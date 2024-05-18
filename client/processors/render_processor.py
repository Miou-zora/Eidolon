import esper
import pyray

from client.components.drawable import Drawable
from client.resources.assets_manager import AssetsManager
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        pyray.draw_text(
            "Congrats! You created your first window!", 190, 200, 20, pyray.LIGHTGRAY
        )
        for ent, (pos, drawable) in esper.get_components(Position, Drawable):
            texture = r.get_resource(AssetsManager).get_texture(drawable.texture_name)
            if texture is not None:
                pyray.draw_texture(texture, pos.x, pos.y, pyray.WHITE)
        pyray.end_drawing()
