from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING, Optional

import pyray as raylib

from common.engine.resource import Resource

if TYPE_CHECKING:
    from common.engine.engine import Engine


class AssetsManager(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.textures: dict[str, raylib.Texture] = {}
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
        self.textures[texture_name] = texture

    def get_texture(self, texture_name: str) -> Optional[raylib.Texture]:
        return self.textures[texture_name]

    def get_texture_size(self, asset_name) -> (int, int):
        texture = self.get_texture(asset_name)
        return texture.width, texture.height
