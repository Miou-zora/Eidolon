import pyray as raylib

from common.engine.engine import Engine
from common.engine.resource import Resource


class InputsManager(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self._keys: dict[raylib.KeyboardKey, bool] = {}
        self._mouse_buttons: dict[raylib.MouseButton, bool] = {}
        self._mouse_wheel: int = 0
        self._mouse_position: raylib.Vector2 = raylib.Vector2(0, 0)

    def is_key_pressed(self, key: raylib.KeyboardKey) -> bool:
        return raylib.is_key_pressed(key)

    def is_key_down(self, key: raylib.KeyboardKey) -> bool:
        if key in self._keys:
            return self._keys[key]
        return False

    def is_mouse_button_pressed(self, button: raylib.MouseButton) -> bool:
        if button in self._mouse_buttons:
            return self._mouse_buttons[button]
        return False

    def get_mouse_wheel(self) -> int:
        return self._mouse_wheel

    def get_mouse_position(self) -> raylib.Vector2:
        return self._mouse_position

    def update(self):
        self._keys = {key: raylib.is_key_down(key) for key in raylib.KeyboardKey}
        self._mouse_buttons = {
            button: raylib.is_mouse_button_down(button) for button in raylib.MouseButton
        }
        self._mouse_wheel = raylib.get_mouse_wheel_move()
        self._mouse_position = raylib.get_mouse_position()
