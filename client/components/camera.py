from common.engine import component
from common.utils.debug import Debug
from common.utils.vector2 import Vector2


@component
class Camera2D(Debug):
    offset: Vector2
    rotation: float
    zoom: float
    id: int
