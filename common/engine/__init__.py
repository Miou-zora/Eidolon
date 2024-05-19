from dataclasses import dataclass as component

from .entity import Entity, EntityId
from .processor import Processor, ProcessorClass
from .resource import Resource
from .resource_manager import ResourceManager
from .time import TimeUnit

__all__ = (
    "Entity",
    "EntityId",
    "component",
    "TimeUnit",
    "Processor",
    "ProcessorClass",
    "Resource",
    "ResourceManager",
)
