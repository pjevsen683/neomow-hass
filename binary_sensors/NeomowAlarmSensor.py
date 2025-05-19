from .NeomowBaseBinarySensor import NeomowBaseBinarySensor
from ..coordinator import NeomowCoordinator

class NeomowAlarmSensor(NeomowBaseBinarySensor):
    """Alarm sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the alarm sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Alarm"
        self._attr_unique_id = f"{coordinator._device_id}_alarm"
        self._attr_device_class = "problem"

    @property
    def is_on(self) -> bool:
        """Return true if there is an alarm."""
        if not self.coordinator.data:
            return False
        return self.coordinator.data.get("alarm", {}).get("active") == "on"
