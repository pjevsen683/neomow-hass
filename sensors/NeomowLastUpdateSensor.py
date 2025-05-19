from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator
from datetime import datetime

class NeomowLastUpdateSensor(NeomowBaseSensor):
    """Last update sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the last update sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Last Update"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_last_update"
        self._attr_object_id = f"neomow_{coordinator._device_id}_last_update"
        self._attr_device_class = "timestamp"

    @property
    def native_value(self) -> datetime | None:
        """Return the last update timestamp."""
        if not self.coordinator.data:
            return None
        timestamp_str = self.coordinator.data.get("timestamp")
        if timestamp_str:
            try:
                return datetime.fromisoformat(timestamp_str)
            except (ValueError, TypeError):
                return None
        return None
