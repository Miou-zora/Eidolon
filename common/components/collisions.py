import enum
from dataclasses import dataclass, field

from common.engine import component
from common.utils.vector2 import Vector2


class CollisionDirection(enum.Enum):
    UP = enum.auto()
    DOWN = enum.auto()
    LEFT = enum.auto()
    RIGHT = enum.auto()


@dataclass
class Collision:

    entity: int
    direction: CollisionDirection


@component
class Collisions:
    collisions_between_entity: list[Collision] = field(default_factory=list)
    last_position: Vector2 = Vector2(0, 0)
