import esper
import raylib

from client.components.drawable import Drawable
from client.resources.assets_manager import AssetsManager
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        raylib.BeginDrawing()
        raylib.ClearBackground(raylib.RAYWHITE)
        raylib.DrawText(
            b"Congrats! You created your first window!", 190, 200, 20, raylib.LIGHTGRAY
        )
        for ent, (pos, drawable) in esper.get_components(Position, Drawable):
            texture = r.get_resource(AssetsManager).get_texture(drawable.texture_name)
            if texture is not None:
                raylib.DrawTexture(texture, pos.x, pos.y, raylib.WHITE)
        raylib.EndDrawing()
