from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowLatitude(NeomowBaseSensor):
    """Latitude sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the latitude sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Latitude"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_latitude"
        self._attr_object_id = f"neomow_{coordinator._device_id}_latitude"
        self._attr_icon = "mdi:latitude"

    @property
    def native_value(self) -> float | None:
        """Return the latitude."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("latitude") 