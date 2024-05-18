import logging

import esper

from common.components.name import Name
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers import UnitTimeProvider
from common.resources.time_providers.time_provider import TimeProvider

logger = logging.getLogger(__name__)


class LogProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        time_provider: UnitTimeProvider = r.get_resource(TimeProvider)
        if time_provider is None:
            raise NotImplemented(
                f"Resource not found: UnitTimeProvider:{time_provider}"
            )
        logger.info(f"Elapsed time: {time_provider.get_elapsed_time()}")
        for ent, (pos, name) in esper.get_components(Position, Name):
            logger.debug(f"{name}: {pos}")
