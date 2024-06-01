import enum
from dataclasses import dataclass, field

from common.engine import component
from common.utils.vector2 import Vector2


@dataclass
class Collision:
    class Direction(enum.Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    entity: int
    direction: Direction


@component
class Collisions:
    collisions_between_entity: list[Collision] = field(default_factory=list)
    last_position: Vector2 = Vector2(0, 0)
