from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowMowingCoverage(NeomowBaseSensor):
    """Mowing coverage sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the mowing coverage sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Mowing Coverage"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_mowing_coverage"
        self._attr_object_id = f"neomow_{coordinator._device_id}_mowing_coverage"
        self._attr_native_unit_of_measurement = "%"
        self._attr_state_class = "measurement"
        self._attr_icon = "mdi:percent"

    @property
    def native_value(self) -> float | None:
        """Return the mowing coverage rate."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("deviceRegionTask", {}).get("mowingCoverageRate", 0.0) 