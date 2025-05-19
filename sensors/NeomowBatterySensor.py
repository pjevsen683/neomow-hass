from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowBatterySensor(NeomowBaseSensor):
    """Battery sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the battery sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Battery"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_battery"
        self._attr_object_id = f"neomow_{coordinator._device_id}_battery"
        self._attr_native_unit_of_measurement = "%"
        self._attr_device_class = "battery"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the battery level."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("electricity")
