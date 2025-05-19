from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowBatteryTemperatureSensor(NeomowBaseSensor):
    """Battery temperature sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the battery temperature sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Battery Temperature"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_battery_temperature"
        self._attr_object_id = f"neomow_{coordinator._device_id}_battery_temperature"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_device_class = "temperature"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the battery temperature."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("batteryTemp")
