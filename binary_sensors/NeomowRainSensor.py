from .NeomowBaseBinarySensor import NeomowBaseBinarySensor
from ..coordinator import NeomowCoordinator

class NeomowRainSensor(NeomowBaseBinarySensor):
    """Rain sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the rain sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Rain Sensor"
        self._attr_unique_id = f"{coordinator._device_id}_rain_sensor"
        self._attr_device_class = "moisture"

    @property
    def is_on(self) -> bool:
        """Return true if rain is detected."""
        if not self.coordinator.data:
            return False
        return self.coordinator.data.get("rainSensorStatus") == "1" 