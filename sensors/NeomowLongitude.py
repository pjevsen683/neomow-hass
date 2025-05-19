from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowLongitude(NeomowBaseSensor):
    """Longitude sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the longitude sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Longitude"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_longitude"
        self._attr_object_id = f"neomow_{coordinator._device_id}_longitude"
        self._attr_icon = "mdi:longitude"

    @property
    def native_value(self) -> float | None:
        """Return the longitude."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("longitude") 