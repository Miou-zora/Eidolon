from pyray import Color, BLACK

from common.engine import component


@component
class Text:
    value: str = ""
    size: int = 12
    font: str = "default"
    spacing: int = 3
    color: Color = BLACK
    # TODO: find a way to extract this from Text and Drawable components
    z_order: int = 0
    # -1 is no camera
    camera_id: int = -1
