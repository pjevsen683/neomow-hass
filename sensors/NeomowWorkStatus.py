from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowWorkStatus(NeomowBaseSensor):
    """Work status sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the work status sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Work Status"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_work_status"
        self._attr_object_id = f"neomow_{coordinator._device_id}_work_status"
        self._attr_icon = "mdi:robot-mower"

    @property
    def native_value(self) -> str | None:
        """Return the work status."""
        if not self.coordinator.data:
            return None
        
        status = self.coordinator.data.get("workStatus")
        if status == 0:
            return "Idle"
        elif status == 1 or status == 5:
            return "Charging"
        elif status == 2:
            return "Mowing"
        elif status == 3:
            return "Returning"
        else:
            return "Unknown" 