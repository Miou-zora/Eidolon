from common.engine import component
from common.utils.vector2 import Vector2
from common.utils.debug import Debug


@component
class Velocity(Vector2, Debug):

    def __init__(self, x: float = 0, y: float = 0) -> None:
        super().__init__(x, y)

