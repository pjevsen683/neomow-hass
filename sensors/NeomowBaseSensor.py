from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from ..coordinator import NeomowCoordinator
from ..const import DOMAIN

class NeomowBaseSensor(CoordinatorEntity, SensorEntity):
    """Base class for Neomow sensors."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the sensor."""
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
