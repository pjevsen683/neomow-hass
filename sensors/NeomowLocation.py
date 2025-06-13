from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowLocation(NeomowBaseSensor):
    """Location sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the location sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Location"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_location"
        self._attr_object_id = f"neomow_{coordinator._device_id}_location"
        self._attr_device_class = "location"
        self._attr_icon = "mdi:map-marker"
        self._attr_gps_accuracy = 5

    @property
    def native_value(self) -> str | None:
        """Return the location as a comma-separated string."""
        if not self.coordinator.data:
            return None
            
        latitude = self.coordinator.data.get("latitude")
        longitude = self.coordinator.data.get("longitude")
        
        if latitude is None or longitude is None:
            return None
            
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        
        return f"{self.latitude},{self.longitude}"

    @property
    def extra_state_attributes(self) -> dict[str, float]:
        """Return the latitude and longitude as attributes."""
        if not self.coordinator.data:
            return {}
            
        latitude = self.coordinator.data.get("latitude")
        longitude = self.coordinator.data.get("longitude")
        
        if latitude is None or longitude is None:
            return {}
            
        return {
            "latitude": float(latitude),
            "longitude": float(longitude)
        } 