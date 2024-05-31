import logging

import esper
import pyray

from common.components.box_collider import BoxCollider
from common.components.physic_body import Physic
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.camera import Camera2D
from components.drawable import Drawable
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
        assets_manager = r.get_resource(AssetsManager)
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
            texture = assets_manager.get_texture(drawable.texture_name)
            if texture is not None:
                pyray.draw_texture(texture, int(pos.x), int(pos.y), pyray.WHITE)
        for ent, (body, drawable) in esper.get_components(Physic, Drawable):
            texture = assets_manager.get_texture(drawable.texture_name)
            if texture is not None and body.body is not None:
                size = assets_manager.get_texture_size(drawable.texture_name)
                pyray.draw_texture(
                    texture,
                    int(body.body.position.x - size.x / 2),
                    int(body.body.position.y - size.y / 2),
                    pyray.WHITE,
                )
        if DEBUG_COLLIDER:
            for ent, (pos, collider) in esper.get_components(Position, BoxCollider):
                pyray.draw_rectangle_lines_ex(
                    pyray.Rectangle(int(pos.x), int(pos.y), collider.x, collider.y),
                    1,
                    pyray.RED,
                )
            for ent, body in esper.get_component(Physic):
                if body.shape is not None:
                    pyray.draw_rectangle_lines_ex(
                        pyray.Rectangle(
                            int(body.shape.bb.left),
                            int(body.shape.bb.bottom),
                            int(body.shape.bb.right - body.shape.bb.left),
                            int(body.shape.bb.top - body.shape.bb.bottom),
                        ),
                        1,
                        pyray.BLUE,
                    )
        pyray.end_mode_2d()
        pyray.end_drawing()
