from common.engine import component
from common.utils.vector2 import Vector2


@component
class Camera2D:
    offset: Vector2
    rotation: float
    zoom: float
