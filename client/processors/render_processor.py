import esper
import pyray

from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.box_collider import BoxCollider
from components.drawable import Drawable
from resources.assets_manager import AssetsManager
from resources.window_resource import WindowResource

DEBUG_COLLIDER = True


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        window = r.get_resource(WindowResource)
        pyray.begin_drawing()
        pyray.clear_background(window.background_color)
        for ent, (pos, drawable) in esper.get_components(Position, Drawable):
            texture = r.get_resource(AssetsManager).get_texture(drawable.texture_name)
            if texture is not None:
                pyray.draw_texture(texture, int(pos.x), int(pos.y), pyray.WHITE)
            if (
                DEBUG_COLLIDER
                and (collider := esper.component_for_entity(ent, BoxCollider))
                is not None
            ):
                pyray.draw_rectangle_lines_ex(
                    pyray.Rectangle(
                        int(pos.x), int(pos.y), collider.size.x, collider.size.y
                    ),
                    1,
                    pyray.RED,
                )
        pyray.end_drawing()
