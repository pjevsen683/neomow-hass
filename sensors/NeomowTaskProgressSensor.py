from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowTaskProgressSensor(NeomowBaseSensor):
    """Task progress sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the task progress sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Task Progress"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_task_progress"
        self._attr_object_id = f"neomow_{coordinator._device_id}_task_progress"
        self._attr_native_unit_of_measurement = "%"
        self._attr_device_class = "percentage"
        self._attr_state_class = "measurement"

    @property
    def native_value(self) -> float | None:
        """Return the task progress."""
        if not self.coordinator.data:
            return None
        device_region_task = self.coordinator.data.get("deviceRegionTask", {})
        return device_region_task.get("taskProgress", 100.0)
