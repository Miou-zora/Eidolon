import raylib

from common.engine.resource import Resource


class AssetsManager(Resource):
    def __init__(self):
        self.textures: dict[str, raylib.Texture] = {}

    def load_texture(self, texture_name: str, texture_path: str):
        texture: raylib.Texture = raylib.LoadTexture(texture_path)
        result: bool = raylib.IsTextureReady(texture)
        if not result:
            raise ValueError(f"Texture {texture_path} not loaded")
        self.textures[texture_name] = texture

    def get_texture(self, texture_name: str):
        if texture_name in self.textures:
            return self.textures[texture_name]
        return None
