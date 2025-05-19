"""Neomow binary sensors."""

from .NeomowMowingSensor import NeomowMowingSensor
from .NeomowAlarmSensor import NeomowAlarmSensor
from .NeomowRainSensor import NeomowRainSensor  

# List of all sensor classes
ALL_SENSORS = [
    NeomowMowingSensor,
    NeomowAlarmSensor,
    NeomowRainSensor,
]

__all__ = [
    "NeomowMowingSensor",
    "NeomowAlarmSensor",
    "NeomowRainSensor",
    "ALL_SENSORS",
] 
