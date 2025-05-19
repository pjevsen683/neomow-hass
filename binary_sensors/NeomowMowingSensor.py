from .NeomowBaseBinarySensor import NeomowBaseBinarySensor
from ..coordinator import NeomowCoordinator

class NeomowMowingSensor(NeomowBaseBinarySensor):
    """Mowing status sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the mowing sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Mowing"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_mowing"
        self._attr_device_class = "moving"

    @property
    def is_on(self) -> bool:
        """Return true if the mower is mowing."""
        if not self.coordinator.data:
            return False
        # Convert workStatus to int if it's a string, or use as is if it's already an int
        work_status = self.coordinator.data.get("workStatus")
        if isinstance(work_status, str):
            try:
                work_status = int(work_status)
            except ValueError:
                return False
        return work_status == 2
