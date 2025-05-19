from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowTokenSensor(NeomowBaseSensor):
    """Representation of a Neomow token sensor."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Token"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_token"
        self._attr_object_id = f"neomow_{coordinator._device_id}_token"
        self._attr_icon = "mdi:key"
        self._attr_entity_registry_enabled_default = False  # Hide by default

    @property
    def native_value(self):
        """Return the state of the sensor."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("token")
