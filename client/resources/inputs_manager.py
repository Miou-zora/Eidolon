import raylib

from common.engine.resource import Resource


class InputsManager(Resource):
    def __init__(self):
        self._wanted_keys: list[raylib.KeyboardKey] = [
            raylib.KEY_UP,
            raylib.KEY_DOWN,
            raylib.KEY_LEFT,
            raylib.KEY_RIGHT,
            raylib.KEY_A,
            raylib.KEY_B,
            raylib.KEY_C,
            raylib.KEY_D,
            raylib.KEY_E,
            raylib.KEY_F,
            raylib.KEY_G,
            raylib.KEY_H,
            raylib.KEY_I,
            raylib.KEY_J,
            raylib.KEY_K,
            raylib.KEY_L,
            raylib.KEY_M,
            raylib.KEY_N,
            raylib.KEY_O,
            raylib.KEY_P,
            raylib.KEY_Q,
            raylib.KEY_R,
            raylib.KEY_S,
            raylib.KEY_T,
            raylib.KEY_U,
            raylib.KEY_V,
            raylib.KEY_W,
            raylib.KEY_X,
            raylib.KEY_Y,
            raylib.KEY_Z,
        ]
        self._wanted_mouse_buttons: list[raylib.MouseButton] = [
            raylib.MOUSE_BUTTON_BACK,
            raylib.MOUSE_BUTTON_EXTRA,
            raylib.MOUSE_BUTTON_FORWARD,
            raylib.MOUSE_BUTTON_LEFT,
            raylib.MOUSE_BUTTON_MIDDLE,
            raylib.MOUSE_BUTTON_RIGHT,
            raylib.MOUSE_BUTTON_SIDE,
        ]
        self._keys: dict[raylib.KeyboardKey, bool] = {}
        self._mouse_buttons: dict[raylib.MouseButton, bool] = {}
        self._mouse_wheel: int = 0
        self._mouse_position: raylib.Vector2 = raylib.Vector2Zero()

    def is_key_pressed(self, key: int) -> bool:
        if key in self._keys:
            return self._keys[key]
        return False

    def is_mouse_button_pressed(self, button: int) -> bool:
        if button in self._mouse_buttons:
            return self._mouse_buttons[button]
        return False

    def get_mouse_wheel(self) -> int:
        return self._mouse_wheel

    def get_mouse_position(self):
        return self._mouse_position

    def update(self):
        for key in self._wanted_keys:
            self._keys[key] = raylib.IsKeyDown(key)
        for button in self._wanted_mouse_buttons:
            self._mouse_buttons[button] = raylib.IsMouseButtonDown(button)
        self._mouse_wheel = raylib.GetMouseWheelMove()
        self._mouse_position = raylib.GetMousePosition()
