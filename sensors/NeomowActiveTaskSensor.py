from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowActiveTaskSensor(NeomowBaseSensor):
    """Active task sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the active task sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Active Task"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_active_task"
        self._attr_object_id = f"neomow_{coordinator._device_id}_active_task"

    @property
    def native_value(self) -> str | None:
        """Return the active task."""
        if not self.coordinator.data:
            return None
        device_region_task = self.coordinator.data.get("deviceRegionTask", {})
        return device_region_task.get("regionName", "None")
