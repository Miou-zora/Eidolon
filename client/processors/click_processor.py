import logging

import esper
import pyray as raylib

from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.box_collider import BoxCollider
from components.clickable import Clickable
from resources.window_resource import WindowResource

logger = logging.getLogger(__name__)


class ClickProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        window_resource = r.get_resource(WindowResource)
        if not window_resource.is_mouse_button_down_released(
            raylib.MouseButton.MOUSE_BUTTON_LEFT
        ):
            return
        mouse_position: raylib.Vector2 = window_resource.get_mouse_position()
        for ent, (clickable, collider, position) in esper.get_components(
            Clickable, BoxCollider, Position
        ):
            if self.are_position_matching(mouse_position, position, collider):
                clickable()

    def are_position_matching(
        self, mouse_position: raylib.Vector2, position: Position, collider: BoxCollider
    ) -> bool:
        return (
            position.x <= mouse_position.x <= position.x + collider.x
            and position.y <= mouse_position.y <= position.y + collider.y
        )
