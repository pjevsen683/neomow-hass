"""Sensor platform for Neomow integration."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .sensors import *

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the Neomow sensors."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    
    neomow_sensors = []
    for sensor_class in ALL_SENSORS:
        neomow_sensors.append(sensor_class(coordinator))
    
    _LOGGER.debug("Setting up %d sensors", len(neomow_sensors))
    async_add_entities(neomow_sensors)
