import pyray as raylib

from common.engine.engine import Engine
from common.engine.resource import Resource
from common.utils.vector2 import Vector2


class WindowResource(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.background_color: raylib.Color = raylib.RAYWHITE
        raylib.init_window(1600, 900, "Eidolon Engine")

    def is_mouse_button_down_released(self, button: raylib.MouseButton) -> bool:
        return raylib.is_mouse_button_released(button)

    def get_mouse_position(self) -> raylib.Vector2:
        return raylib.get_mouse_position()

    def get_size(self) -> raylib.Vector2:
        return Vector2(raylib.get_screen_width(), raylib.get_screen_height())
