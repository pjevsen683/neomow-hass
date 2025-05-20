"""Coordinator for Neomow integration."""
from __future__ import annotations

import logging
import json
from datetime import datetime, timedelta, timezone
import asyncio
import paho.mqtt.client as mqtt

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_SCAN_INTERVAL
from homeassistant.helpers.storage import Store

from .const import (
    DOMAIN,
    DEFAULT_SCAN_INTERVAL,
    MQTT_BROKER,
    MQTT_PORT,
    MQTT_USERNAME,
    MQTT_PASSWORD,
    MAX_RECONNECT_ATTEMPTS,
    RECONNECT_DELAY,
)

_LOGGER = logging.getLogger(__name__)

class NeomowCoordinator(DataUpdateCoordinator):
    """Neomow coordinator."""

    def __init__(
        self,
        hass: HomeAssistant,
        entry: ConfigEntry,
    ) -> None:
        """Initialize the coordinator."""
        scan_interval = entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL)
        
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=scan_interval),
        )
        
        self._entry = entry
        self._device_id = entry.data["device_id"]
        self._mqtt_client = None
        self._data = {
            "token": None,
            "battery": None,
            "voltage": None,
            "batteryTemp": None,
            "timestamp": None,
            "robotX": None,
            "robotY": None,
            "wifiSignal": None,
            "deviceRegionTask": {"regionName": "None"},
            "workingMode": None,
            "workStatus": None,
            "rainSensorStatus": None,
            "alarm": {"active": "off"},
            "mapData": None,
            "pathList": None,
        }
        self._heartbeat_task = None
        self._reconnect_attempts = 0
        self._reconnect_task = None
        
        # Create store for persisting data
        self._store = Store(hass, 1, f"{DOMAIN}.{self._device_id}")
        
        # Start MQTT client
        self._setup_mqtt()

    async def async_load_data(self) -> None:
        """Load persisted data."""
        if stored := await self._store.async_load():
            self._data.update(stored)
            _LOGGER.debug("Loaded persisted data: %s", stored)

    async def async_save_data(self) -> None:
        """Save data to persistent storage."""
        await self._store.async_save(self._data)
        _LOGGER.debug("Saved data to persistent storage: %s", self._data)

    def _setup_mqtt(self) -> None:
        """Set up MQTT client."""
        try:
            self._mqtt_client = mqtt.Client()
            
            # Set up callbacks
            self._mqtt_client.on_connect = self._on_connect
            self._mqtt_client.on_message = self._on_message
            self._mqtt_client.on_disconnect = self._on_disconnect
            
            # Set credentials
            self._mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
            
            # Connect to Neomow MQTT broker
            _LOGGER.info("Connecting to MQTT broker %s:%d", MQTT_BROKER, MQTT_PORT)
            self._mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
            
            # Start the loop
            self._mqtt_client.loop_start()
            
        except Exception as e:
            _LOGGER.error("Failed to setup MQTT client: %s", str(e))
            self._schedule_reconnect()

    def _on_connect(self, client, userdata, flags, rc) -> None:
        """Handle MQTT connection."""
        if rc == 0:
            _LOGGER.info("Connected to Neomow MQTT broker")
            self._reconnect_attempts = 0  # Reset reconnect attempts on successful connection
            
            # Subscribe to topics
            client.subscribe(f"hookii/heartbeat/app/{self._device_id}")
            client.subscribe(f"hookii/details/device/{self._device_id}")
            
            # Start sending heartbeats using Home Assistant's event loop
            self.hass.loop.call_soon_threadsafe(self._start_heartbeat)
        else:
            error_msg = {
                1: "Connection refused - incorrect protocol version",
                2: "Connection refused - invalid client identifier",
                3: "Connection refused - server unavailable",
                4: "Connection refused - bad username or password",
                5: "Connection refused - not authorized"
            }.get(rc, f"Connection failed with code {rc}")
            
            _LOGGER.error("Failed to connect to Neomow MQTT broker: %s", error_msg)
            self._schedule_reconnect()

    def _on_message(self, client, userdata, msg) -> None:
        """Handle MQTT message."""
        try:
            payload = json.loads(msg.payload.decode())
            msg_type = payload.get("msgType")
            
            if msg_type == "HEARTBEAT":
                if "data" in payload and "token" in payload["data"]:
                    self._data["token"] = payload["data"]["token"]
                    # Save token to persistent storage
                    self.hass.loop.call_soon_threadsafe(
                        lambda: self.hass.async_create_task(self.async_save_data())
                    )
                    # Notify listeners of the update
                    self.hass.loop.call_soon_threadsafe(
                        lambda: self.async_set_updated_data(self._data)
                    )
            elif msg_type == "STATUS":
                if "data" in payload and "STATUS" in payload["data"]:
                    status = payload["data"]["STATUS"]
                    # Add timestamp to status
                    status["timestamp"] = datetime.now().astimezone()
                    
                    # Update data with status
                    self._data.update(status)
                    
                    # Log updated data for debugging
                    _LOGGER.debug("Updated data: %s", self._data)
                    
                    # Notify listeners of the update
                    self.hass.loop.call_soon_threadsafe(
                        lambda: self.async_set_updated_data(self._data)
                    )
            elif msg_type == "NOTICE_ALARM":
                if "data" in payload:
                    self._data["alarm"] = {
                        "active": "on" if len(payload["data"]) > 0 else "off",
                        "details": payload["data"]
                    }
                    # Notify listeners of the update
                    self.hass.loop.call_soon_threadsafe(
                        lambda: self.async_set_updated_data(self._data)
                    )
            elif msg_type == "DEVICE_MAP_V2":
                _LOGGER.info("Received message: DEVICE_MAP_V2")
                # Make an svg map and save the file somewhere. the data is too big to handle in db.
                
            elif msg_type == "ALL_PATH_LIST_V2":
                _LOGGER.info("Received message: ALL_PATH_LIST_V2")
                # Make an svg map and save the file somewhere. the data is too big to handle in db.
            
        except json.JSONDecodeError:
            _LOGGER.error("Failed to decode MQTT message: %s", msg.payload)

    def _on_disconnect(self, client, userdata, rc) -> None:
        """Handle MQTT disconnection."""
        if rc != 0:
            _LOGGER.warning("Unexpectedly disconnected from Neomow MQTT broker (code: %d)", rc)
            self._schedule_reconnect()
        else:
            _LOGGER.info("Disconnected from Neomow MQTT broker")

    def _schedule_reconnect(self) -> None:
        """Schedule a reconnection attempt."""
        if self._reconnect_task is not None:
            self._reconnect_task.cancel()
            
        if self._reconnect_attempts >= MAX_RECONNECT_ATTEMPTS:
            _LOGGER.error("Maximum reconnection attempts reached")
            return
            
        self._reconnect_attempts += 1
        delay = RECONNECT_DELAY * self._reconnect_attempts
        
        async def reconnect():
            _LOGGER.info("Attempting to reconnect in %d seconds (attempt %d/%d)",
                        delay, self._reconnect_attempts, MAX_RECONNECT_ATTEMPTS)
            await asyncio.sleep(delay)
            self._setup_mqtt()
            
        self._reconnect_task = asyncio.create_task(reconnect())

    def _start_heartbeat(self) -> None:
        """Start sending heartbeat messages."""
        if self._heartbeat_task is not None:
            self._heartbeat_task.cancel()
            
        async def send_heartbeat():
            while True:
                if self._data["token"]:
                    message = {
                        "ts": int(datetime.now().timestamp() * 1000),
                        "msgType": "HEARTBEAT",
                        "data": {
                            "push": 523,
                            "token": self._data["token"]
                        }
                    }
                    self._mqtt_client.publish(
                        f"hookii/heartbeat/app/{self._device_id}",
                        json.dumps(message)
                    )
                await asyncio.sleep(self.update_interval.total_seconds())
        
        self._heartbeat_task = asyncio.create_task(send_heartbeat())

    async def _async_update_data(self):
        """Update data."""
        return self._data

    async def async_shutdown(self) -> None:
        """Shutdown the coordinator."""
        if self._heartbeat_task is not None:
            self._heartbeat_task.cancel()
            self._heartbeat_task = None
            
        if self._reconnect_task is not None:
            self._reconnect_task.cancel()
            self._reconnect_task = None
            
        if self._mqtt_client:
            self._mqtt_client.loop_stop()
            self._mqtt_client.disconnect() 