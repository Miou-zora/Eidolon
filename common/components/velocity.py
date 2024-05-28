from common.engine import component
from common.utils.vector2 import Vector2


@component
class Velocity(Vector2):

    def __init__(self, x: float = 0, y: float = 0) -> None:
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"Velocity({self.x},{self.y})"
