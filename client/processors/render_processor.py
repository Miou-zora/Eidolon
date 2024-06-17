from __future__ import annotations

import logging
from typing import TYPE_CHECKING

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

if TYPE_CHECKING:
    from typing import Callable

    map_layer_by_draw_function = dict[int, list[tuple[int, Callable[[], None]]]]

DEBUG_COLLIDER = True

logger = logging.getLogger(__name__)


class RenderProcessor(Processor):
    __default_camera = pyray.Camera2D((0, 0), (0, 0), 0, 1)

    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        window = r.get_resource(WindowResource)
        assets_manager = r.get_resource(AssetsManager)
        pyray.clear_background(window.background_color)
        to_draw: map_layer_by_draw_function = {}
        RenderProcessor.__register_textures_to_draw(assets_manager, to_draw)
        RenderProcessor.__register_text_to_draw(to_draw, r)
        if (
            DEBUG_COLLIDER
        ):  # This should be temporary until we find a better way to debug colliders
            for ent, (pos, collider) in esper.get_components(Position,
                                                             BoxCollider):
                to_draw.setdefault(100, []).append(
                    (0, RenderProcessor.__create_draw_rectangle_lines_ex(pos,
                                                                         collider))
                )
        RenderProcessor.__draw_layers(to_draw)

    @staticmethod
    def __draw_layers(to_draw: map_layer_by_draw_function):
        cameras = esper.get_components(Camera2D, Position)
        camera_by_id: dict[int, tuple[Camera2D, Position]] = {
            camera[1][0].id: (camera[1][0], camera[1][1]) for camera in cameras
        }
        current_camera_id: int = -1
        pyray.begin_mode_2d(RenderProcessor.__default_camera)
        for layer in sorted(to_draw.keys()):
            RenderProcessor.__draw_layer(
                to_draw[layer], camera_by_id, current_camera_id
            )
        pyray.end_mode_2d()

    @staticmethod
    def __draw_layer(
        to_draw_layer: list[tuple[int, Callable[[], None]]],
        camera_by_id: dict[int, tuple[Camera2D, Position]],
        current_camera_id: int,
    ):
        for camera_id, draw in to_draw_layer:
            if camera_id != current_camera_id:
                current_camera_id = camera_id
                pyray.end_mode_2d()
                if camera_id == -1:
                    pyray.begin_mode_2d(RenderProcessor.__default_camera)
                else:
                    camera = camera_by_id.get(camera_id)
                    if camera is None:
                        logger.warning(f"Camera with id {camera_id} not found")
                        pyray.begin_mode_2d(RenderProcessor.__default_camera)
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

    @staticmethod
    def __register_textures_to_draw(
        assets_manager: AssetsManager, to_draw: map_layer_by_draw_function
    ) -> None:
        for ent, (pos, drawable) in esper.get_components(Position, Drawable):
            texture = assets_manager.get_texture(drawable.texture_name)
            if texture is not None:
                to_draw.setdefault(drawable.z_order, []).append(
                    (
                        drawable.camera_id,
                        RenderProcessor.__create_draw_texture(texture, pos),
                    )
                )

    @staticmethod
    def __register_text_to_draw(
        to_draw: map_layer_by_draw_function, r: ResourceManager
    ) -> None:
        for ent, (pos, text) in esper.get_components(Position, Text):
            to_draw.setdefault(text.z_order, []).append(
                (text.camera_id,
                 RenderProcessor.__create_draw_text_ex(r, text, pos))
            )

    @staticmethod
    def __create_draw_text_ex(r, text, pos) -> Callable[[], None]:
        return lambda: pyray.draw_text_ex(
            r.get_resource(AssetsManager).get_font(text.font),
            text.value,
            pyray.Vector2(pos.x, pos.y),
            text.size,
            text.spacing,
            text.color,
        )

    @staticmethod
    def __create_draw_rectangle_lines_ex(pos, collider) -> Callable[[], None]:
        return lambda: pyray.draw_rectangle_lines_ex(
            pyray.Rectangle(int(pos.x), int(pos.y), collider.x, collider.y),
            1,
            pyray.RED,
        )

    @staticmethod
    def __create_draw_texture(texture, pos) -> Callable[[], None]:
        return lambda: pyray.draw_texture(
            texture,
            int(pos.x),
            int(pos.y),
            pyray.WHITE,
        )
