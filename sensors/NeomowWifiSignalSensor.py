from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowWifiSignalSensor(NeomowBaseSensor):
    """WiFi signal sensor for Neomow."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the WiFi signal sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} WiFi Signal"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_wifi_signal"
        self._attr_object_id = f"neomow_{coordinator._device_id}_wifi_signal"
        self._attr_device_class = "signal_strength"
        self._attr_native_unit_of_measurement = "dBm"

    @property
    def native_value(self) -> int | None:
        """Return the WiFi signal strength."""
        if not self.coordinator.data:
            return None
        return self.coordinator.data.get("wifiSignal")
