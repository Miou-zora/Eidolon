import enum
from dataclasses import dataclass

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


class Collisions:
    collisions_between_entity: list[Collision] = []
    last_position: Vector2 = Vector2(0, 0)
