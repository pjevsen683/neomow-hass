from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from ..coordinator import NeomowCoordinator

from ..const import DOMAIN

class NeomowBaseBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Base class for Neomow binary sensors."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator._device_id)},
            name=f"Neomow {coordinator._device_id}",
            manufacturer="Neomow",
            model="Neomow Robot Mower",
        )

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self.coordinator.data is not None
