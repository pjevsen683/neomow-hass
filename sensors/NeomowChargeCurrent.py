from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowChargeCurrent(NeomowBaseSensor):
    """Charge current sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the charge current sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Charge Current"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_charge_current"
        self._attr_object_id = f"neomow_{coordinator._device_id}_charge_current"
        self._attr_native_unit_of_measurement = "A"
        self._attr_device_class = "current"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:current-ac"

    @property
    def native_value(self) -> float | None:
        """Return the charge current."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("chargeCurrent", 0.0) 