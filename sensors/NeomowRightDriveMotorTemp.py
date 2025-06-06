from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowRightDriveMotorTemp(NeomowBaseSensor):
    """Right drive motor temperature sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the right drive motor temperature sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Right Drive Motor Temperature"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_right_drive_motor_temp"
        self._attr_object_id = f"neomow_{coordinator._device_id}_right_drive_motor_temp"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_device_class = "temperature"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:thermometer"

    @property
    def native_value(self) -> float | None:
        """Return the right drive motor temperature."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("rightDriveMotorTemp", 0.0) 