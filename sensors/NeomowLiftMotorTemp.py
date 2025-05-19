from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowLiftMotorTemp(NeomowBaseSensor):
    """Lift motor temperature sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the lift motor temperature sensor."""
        super().__init__(coordinator)
        self._attr_name = f"{coordinator._device_id} Lift Motor Temperature"
        self._attr_unique_id = f"{coordinator._device_id}_lift_motor_temp"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_device_class = "temperature"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:thermometer"

    @property
    def native_value(self) -> float | None:
        """Return the lift motor temperature."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("liftMotorTemp", 0.0) 