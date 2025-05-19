from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowGridZone(NeomowBaseSensor):
    """Grid zone sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the grid zone sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Grid Zone"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_grid_zone"
        self._attr_object_id = f"neomow_{coordinator._device_id}_grid_zone"
        self._attr_icon = "mdi:map"

    @property
    def native_value(self) -> float | None:
        """Return the grid zone."""
        if not self.coordinator.data:
            return None
        # get robot x and y position and make a zone being 10cm x 10cm
        robot_x = self.coordinator.data.get("robotX",0) / 10
        robot_y = self.coordinator.data.get("robotY",0) / 10
        zone = str(int(robot_x)) + "," + str(int(robot_y))
        return zone
