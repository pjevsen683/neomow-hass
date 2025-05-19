from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowOnlineStatus(NeomowBaseSensor):
    """Online status sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the online status sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Online Status"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_online"
        self._attr_object_id = f"neomow_{coordinator._device_id}_online_status"
        self._attr_icon = "mdi:connection"

    @property
    def native_value(self) -> str | None:
        """Return the online status."""
        if not self.coordinator.data:
            return None
        
        status = self.coordinator.data.get("onlineStatus")
        if status == 1:
            return "Online"
        elif status == 3:
            return "Sleeping"
        else:
            return "Offline" 