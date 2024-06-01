from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING

import pyray as raylib

from common.engine.resource import Resource
from common.utils.vector2 import Vector2

if TYPE_CHECKING:
    from common.engine.engine import Engine


class AssetsManager(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        default_texture = raylib.load_texture_from_image(
            raylib.gen_image_checked(100, 100, 50, 50, raylib.PINK, raylib.BLACK)
        )
        self.__textures: dict[str, raylib.Texture] = {"default": default_texture}
        self.__font: dict[str, raylib.Font] = {"default": raylib.get_font_default()}
        self.base_path: str = self.__get_base_path()

    @staticmethod
    def __get_base_path() -> str:
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            return sys._MEIPASS + "/client"
        except Exception:
            base_path = os.path.abspath(".")  # This allows to run __main__ directly
            if not base_path.endswith("client"):
                return os.path.abspath("./client")
            return base_path

    def load_texture(self, texture_name: str, texture_path: str):
        if not raylib.is_window_ready():
            raise ValueError("Raylib is not ready to load textures")
        texture: raylib.Texture = raylib.load_texture(
            os.path.join(self.base_path, texture_path)
        )
        result = raylib.is_texture_ready(texture)
        if not result:
            raise ValueError(
                f"Texture {self.base_path + '/' + texture_path} not loaded"
            )
        self.__textures[texture_name] = texture

    def get_texture(self, texture_name: str) -> raylib.Texture:
        return self.__textures.get(texture_name, self.__textures["default"])

    def get_font(self, font_name: str) -> raylib.Font:
        return self.__font.get(font_name, self.__font["default"])

    def get_texture_size(self, asset_name) -> Vector2:
        texture = self.get_texture(asset_name)
        if texture is None:
            raise KeyError(f"Texture {asset_name} not found")
        return Vector2(texture.width, texture.height)
