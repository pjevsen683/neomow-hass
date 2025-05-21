from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowKnifeDiscMotorSpeed(NeomowBaseSensor):
    """Knife disc motor speed sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the knife disc motor speed sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Knife Disc Motor Speed"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_knife_disc_motor_speed"
        self._attr_object_id = f"neomow_{coordinator._device_id}_knife_disc_motor_speed"
        self._attr_native_unit_of_measurement = "rpm"
        self._attr_device_class = "speed"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:saw-blade"

    @property
    def native_value(self) -> float | None:
        """Return the knife disc motor speed."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("knifeDiscMotorSpeed", 0.0) 
