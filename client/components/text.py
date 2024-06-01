from pyray import Color, BLACK

from common.engine import component


@component
class Text:
    value: str = ""
    size: int = 12
    font: str = "default"
    spacing: int = 3
    color: Color = BLACK
