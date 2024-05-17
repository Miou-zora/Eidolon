from dataclasses import dataclass as component

from .entity import Entity, EntityId
from .processor import Processor, ProcessorClass
from .time import TimeUnit
from .time_provider import TimeProvider

__all__ = (
    "Entity",
    "EntityId",
    "component",
    "TimeProvider",
    "TimeUnit",
    "Processor",
    "ProcessorClass",
)
