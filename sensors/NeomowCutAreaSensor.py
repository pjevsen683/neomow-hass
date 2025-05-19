from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowCutAreaSensor(NeomowBaseSensor):
    """Cut area sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the cut area sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Cut Area"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_cut_area"
        self._attr_object_id = f"neomow_{coordinator._device_id}_cut_area"
        self._attr_native_unit_of_measurement = "m²"
        self._attr_device_class = "area"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the cut area."""
        if not self.coordinator.data:
            return None
        device_region_task = self.coordinator.data.get("deviceRegionTask", {})
        return device_region_task.get("cutArea", 0.0)
