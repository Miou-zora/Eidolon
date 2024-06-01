import logging

import esper

from common.components.name import Name
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.engine.time_providers import RealTimeProvider

logger = logging.getLogger(__name__)


class LogProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        logger.info(f"Elapsed time: {r.get_resource(RealTimeProvider).get_elapsed_time()}")
        for ent, (pos, name) in esper.get_components(Position, Name):
            logger.debug(f"{name}: {pos}")
