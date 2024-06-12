from common.engine import component
from common.utils.vector2 import Vector2
from common.utils.debug import Debug

@component
class Camera2D(Debug):
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

