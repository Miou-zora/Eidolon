from common.engine import component
from common.utils.vector2 import Vector2


@component
class BoxCollider:
    size: Vector2

    def __str__(self) -> str:
        return f"BoxCollider(width:{self.size.x:.6f}, height:{self.size.y:.6f})"
