from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowBatteryVoltageSensor(NeomowBaseSensor):
    """Battery voltage sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the battery voltage sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Battery Voltage"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_battery_voltage"
        self._attr_object_id = f"neomow_{coordinator._device_id}_battery_voltage"
        self._attr_native_unit_of_measurement = "V"
        self._attr_device_class = "voltage"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the battery voltage."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("voltage")
