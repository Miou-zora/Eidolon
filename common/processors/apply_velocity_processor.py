import logging

import esper

from common.components.position import Position
from common.components.velocity import Velocity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.engine.time_providers import RealTimeProvider

logger = logging.getLogger(__name__)


class ApplyVelocityProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        time_provider = r.get_resource(RealTimeProvider)
        for ent, (pos, vel) in esper.get_components(Position, Velocity):
            pos.x += vel.x * time_provider.get_elapsed_time()
            pos.y += vel.y * time_provider.get_elapsed_time()
