from dataclasses import field

from common.engine import component
from common.engine.entity import EntityId


@component
class DrawInventory:
    items: list[EntityId] = field(default_factory=list)
