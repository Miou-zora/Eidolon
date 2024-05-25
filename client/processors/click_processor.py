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
        rl = window_resource.is_mouse_button_down_released(
            raylib.MouseButton.MOUSE_BUTTON_LEFT
        )
        if not rl:
            return
        mouse_position: raylib.Vector2 = window_resource.get_mouse_position()
        for ent, (clickable, collider, position) in esper.get_components(
            Clickable, BoxCollider, Position
        ):
            if self.are_position_matching(mouse_position, position, collider):
                clickable.call()

    def are_position_matching(
        self, mouse_position: raylib.Vector2, position: Position, collider: BoxCollider
    ) -> bool:
        return (
            position.x <= mouse_position.x <= position.x + collider.size.x
            and position.y <= mouse_position.y <= position.y + collider.size.y
        )
