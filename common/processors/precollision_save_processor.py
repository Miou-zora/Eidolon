import logging

import esper

from common.components.collisions import Collisions
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.utils.vector2 import Vector2

logger = logging.getLogger(__name__)


class PreCollisionSaveProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        for ent, (pos, collisions) in esper.get_components(Position, Collisions):
            collisions.last_position = Vector2(pos.x, pos.y)
