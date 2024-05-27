import logging

import esper

from common.components.velocity import Velocity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager

logger = logging.getLogger(__name__)


class ResetVelocityProcessor(Processor):
    def process(self, _: ResourceManager) -> None:
        for ent, vel in esper.get_component(Velocity):
            vel.x = 0
            vel.y = 0
