"""Binary sensor platform for Neomow integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .binary_sensors import *

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Neomow binary sensors."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    # Create binary sensors
    neomow_binary_sensors = []
    for sensor_class in ALL_SENSORS:
        neomow_binary_sensors.append(sensor_class(coordinator))
    
    _LOGGER.debug("Setting up %d binary sensors", len(neomow_binary_sensors))
    async_add_entities(neomow_binary_sensors)
