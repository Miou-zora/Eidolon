from typing import Union

import pyray

from common.engine.resource import Resource


class AssetsManager(Resource):
    def __init__(self):
        self.textures: dict[str, pyray.Texture] = {}

    def load_texture(self, texture_name: str, texture_path: str):
        texture: pyray.Texture = pyray.load_texture(texture_path)
        result: bool = pyray.is_texture_ready(texture)
        if not result:
            raise ValueError(f"Texture {texture_path} not loaded")
        self.textures[texture_name] = texture

    def get_texture(self, texture_name: str) -> Union[pyray.Texture, None]:
        if texture_name in self.textures:
            return self.textures[texture_name]
        return None
