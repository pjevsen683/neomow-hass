from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowXPositionSensor(NeomowBaseSensor):
    """X position sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the X position sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} X Position"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_position_x"
        self._attr_object_id = f"neomow_{coordinator._device_id}_position_x"
        self._attr_native_unit_of_measurement = "m"
        self._attr_device_class = "distance"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the X position."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("robotX")
