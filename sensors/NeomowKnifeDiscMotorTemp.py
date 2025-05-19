from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowKnifeDiscMotorTemp(NeomowBaseSensor):
    """Knife disc motor temperature sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the knife disc motor temperature sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Knife Disc Motor Temperature"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_knife_disc_motor_temp"
        self._attr_object_id = f"neomow_{coordinator._device_id}_knife_disc_motor_temp"
        self._attr_native_unit_of_measurement = "°C"
        self._attr_device_class = "temperature"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:thermometer"

    @property
    def native_value(self) -> float | None:
        """Return the knife disc motor temperature."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("knifeDiscMotorTemp", 0.0) 