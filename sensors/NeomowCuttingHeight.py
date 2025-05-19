from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowCuttingHeight(NeomowBaseSensor):
    """Cutting height sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the cutting height sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Cutting Height"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_cutting_height"
        self._attr_object_id = f"neomow_{coordinator._device_id}_cutting_height"
        self._attr_native_unit_of_measurement = "cm"
        self._attr_device_class = "length"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:height"

    @property
    def native_value(self) -> float | None:
        """Return the cutting height."""
        if not self.coordinator.data:
            return None
        device_region_task = self.coordinator.data.get("deviceRegionTask", {})
        return device_region_task.get("mowingHeight", 0.0)
