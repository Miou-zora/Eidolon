import logging

import esper
import pyray

from common.components.box_collider import BoxCollider
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.camera import Camera2D
from components.drawable import Drawable
from components.text import Text
from resources.assets_manager import AssetsManager
from resources.window_resource import WindowResource

DEBUG_COLLIDER = True

logger = logging.getLogger(__name__)


def create_draw_text_ex(r, text, pos):
    return lambda: pyray.draw_text_ex(
        r.get_resource(AssetsManager).get_font(text.font),
        text.value,
        pyray.Vector2(pos.x, pos.y),
        text.size,
        text.spacing,
        text.color,
    )


def create_draw_rectangle_lines_ex(pos, collider):
    return lambda: pyray.draw_rectangle_lines_ex(
        pyray.Rectangle(int(pos.x), int(pos.y), collider.x, collider.y),
        1,
        pyray.RED,
    )


def create_draw_texture(texture, pos):
    return lambda: pyray.draw_texture(texture, int(pos.x), int(pos.y), pyray.WHITE)


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        window = r.get_resource(WindowResource)
        cameras = esper.get_components(Camera2D, Position)
        assets_manager = r.get_resource(AssetsManager)
        if len(cameras) < 1:
            return
        # main_camera_obj, main_camera_pos = cameras[0][1]
        pyray.clear_background(window.background_color)
        # pyray.begin_mode_2d(
        #     pyray.Camera2D(
        #         (main_camera_obj.offset.x, main_camera_obj.offset.y),
        #         (main_camera_pos.x, main_camera_pos.y),
        #         main_camera_obj.rotation,
        #         main_camera_obj.zoom,
        #     )
        # )
        to_draw: dict[int, list[(int, callable)]] = {}
        for ent, (pos, drawable) in esper.get_components(Position, Drawable):
            texture = assets_manager.get_texture(drawable.texture_name)
            if texture is not None:
                to_draw.setdefault(drawable.z_order, []).append(
                    (drawable.camera_id, create_draw_texture(texture, pos))
                )
        for ent, (pos, text) in esper.get_components(Position, Text):
            to_draw.setdefault(text.z_order, []).append(
                (text.camera_id, create_draw_text_ex(r, text, pos))
            )
        if DEBUG_COLLIDER:
            for ent, (pos, collider) in esper.get_components(Position, BoxCollider):
                to_draw.setdefault(100, []).append(
                    (0, create_draw_rectangle_lines_ex(pos, collider))
                )
        camera_by_id = {
            cameras[i][1][0].id: (cameras[i][1][0], cameras[i][1][1])
            for i in range(len(cameras))
        }
        current_camera_id: int = -1
        default_camera = pyray.Camera2D((0, 0), (0, 0), 0, 1)
        pyray.begin_mode_2d(default_camera)
        for layer in sorted(to_draw.keys()):
            for camera_id, draw in to_draw[layer]:
                if camera_id != current_camera_id:
                    current_camera_id = camera_id
                    pyray.end_mode_2d()
                    if camera_id == -1:
                        pyray.begin_mode_2d(default_camera)
                    else:
                        camera = camera_by_id.get(camera_id)
                        if camera is None:
                            logger.warning(f"Camera with id {camera_id} not found")
                            pyray.begin_mode_2d(default_camera)
                        else:
                            pyray.begin_mode_2d(
                                pyray.Camera2D(
                                    (camera[0].offset.x, camera[0].offset.y),
                                    (camera[1].x, camera[1].y),
                                    camera[0].rotation,
                                    camera[0].zoom,
                                )
                            )
                draw()
        pyray.end_mode_2d()
