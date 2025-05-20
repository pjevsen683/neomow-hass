"""Neomow sensors."""
from .NeomowTokenSensor import NeomowTokenSensor
from .NeomowBatterySensor import NeomowBatterySensor
from .NeomowBatteryVoltageSensor import NeomowBatteryVoltageSensor
from .NeomowBatteryTemperatureSensor import NeomowBatteryTemperatureSensor
from .NeomowLastUpdateSensor import NeomowLastUpdateSensor
from .NeomowXPositionSensor import NeomowXPositionSensor
from .NeomowYPositionSensor import NeomowYPositionSensor
from .NeomowWifiSignalSensor import NeomowWifiSignalSensor
from .NeomowActiveTaskSensor import NeomowActiveTaskSensor
from .NeomowTaskProgressSensor import NeomowTaskProgressSensor
from .NeomowCutAreaSensor import NeomowCutAreaSensor
from .NeomowUncutAreaSensor import NeomowUncutAreaSensor
from .NeomowCuttingHeight import NeomowCuttingHeight
from .NeomowLeftDriveMotorTemp import NeomowLeftDriveMotorTemp
from .NeomowRightDriveMotorTemp import NeomowRightDriveMotorTemp
from .NeomowKnifeDiscMotorTemp import NeomowKnifeDiscMotorTemp  
from .NeomowLocation import NeomowLocation
from .NeomowChargeCurrent import NeomowChargeCurrent
from .NeomowMowingCoverage import NeomowMowingCoverage
from .NeomowOnlineStatus import NeomowOnlineStatus
from .NeomowWorkStatus import NeomowWorkStatus
from .NeomowLatitude import NeomowLatitude
from .NeomowLongitude import NeomowLongitude
from .NeomowGridZone import NeomowGridZone

# List of all sensor classes
ALL_SENSORS = [
    NeomowTokenSensor,
    NeomowBatterySensor,
    NeomowBatteryVoltageSensor,
    NeomowBatteryTemperatureSensor,
    NeomowLastUpdateSensor,
    NeomowXPositionSensor,
    NeomowYPositionSensor,
    NeomowWifiSignalSensor,
    NeomowActiveTaskSensor,
    NeomowTaskProgressSensor,
    NeomowCutAreaSensor,
    NeomowUncutAreaSensor,
    NeomowCuttingHeight,
    NeomowLeftDriveMotorTemp,
    NeomowRightDriveMotorTemp,
    NeomowKnifeDiscMotorTemp,
    NeomowLocation,
    NeomowChargeCurrent,
    NeomowMowingCoverage,
    NeomowOnlineStatus,
    NeomowWorkStatus,
    NeomowLatitude,
    NeomowLongitude,
    NeomowGridZone,
]

__all__ = [
    "NeomowTokenSensor",
    "NeomowBatterySensor",
    "NeomowBatteryVoltageSensor",
    "NeomowBatteryTemperatureSensor",
    "NeomowLastUpdateSensor",
    "NeomowXPositionSensor",
    "NeomowYPositionSensor",
    "NeomowWifiSignalSensor",
    "NeomowActiveTaskSensor",
    "NeomowTaskProgressSensor",
    "NeomowCutAreaSensor",
    "NeomowUncutAreaSensor",
    "NeomowCuttingHeight",
    "NeomowLeftDriveMotorTemp",
    "NeomowRightDriveMotorTemp",
    "NeomowKnifeDiscMotorTemp",
    "NeomowLocation",
    "NeomowChargeCurrent",
    "NeomowMowingCoverage",
    "NeomowOnlineStatus",
    "NeomowWorkStatus",
    "NeomowLatitude",
    "NeomowLongitude",
    "NeomowGridZone",
    "ALL_SENSORS",
] 