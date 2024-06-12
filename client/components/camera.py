from common.engine import component
from common.utils.vector2 import Vector2


@component
class Camera2D:
    offset: Vector2
    rotation: float
    zoom: float
    id: int

    def __init__(
        self, offset: Vector2, rotation: float, zoom: float, _id: int = -1
    ) -> None:
        self.offset = offset
        self.rotation = rotation
        self.zoom = zoom
        self.id = _id

    def __str__(self) -> str:
        return f"Camera2DComponent(offset:{self.offset}, rotation:{self.rotation}, zoom:{self.zoom})"
