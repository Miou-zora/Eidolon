import logging

import esper
import pyray

from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.box_collider import BoxCollider
from components.camera import Camera2D
from components.drawable import Drawable
from components.text import Text
from resources.assets_manager import AssetsManager
from resources.window_resource import WindowResource

DEBUG_COLLIDER = True

logger = logging.getLogger(__name__)


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        window = r.get_resource(WindowResource)
        cameras = esper.get_components(Camera2D, Position)
        if len(cameras) < 1:
            return
        main_camera_obj, main_camera_pos = cameras[0][1]
        pyray.begin_drawing()  # TODO: split begin drawing, draw and end drawing into processor and create a new plugin for rendering
        pyray.clear_background(window.background_color)
        pyray.begin_mode_2d(
            pyray.Camera2D(
                (main_camera_obj.offset.x, main_camera_obj.offset.y),
                (main_camera_pos.x, main_camera_pos.y),
                main_camera_obj.rotation,
                main_camera_obj.zoom,
            )
        )
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
        for ent, (pos, text) in esper.get_components(Position, Text):
            pyray.draw_text_ex(
                r.get_resource(AssetsManager).get_font(text.font),
                text.value,
                pyray.Vector2(pos.x, pos.y),
                text.size,
                text.spacing,
                text.color,
            )
        pyray.end_mode_2d()
        pyray.end_drawing()
