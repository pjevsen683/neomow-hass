from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowUncutAreaSensor(NeomowBaseSensor):
    """Uncut area sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the uncut area sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Uncut Area"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_uncut_area"
        self._attr_object_id = f"neomow_{coordinator._device_id}_uncut_area"
        self._attr_native_unit_of_measurement = "m²"
        self._attr_device_class = "area"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the uncut area."""
        if not self.coordinator.data:
            return None
        device_region_task = self.coordinator.data.get("deviceRegionTask", {})
        return device_region_task.get("uncutArea", 0.0) 