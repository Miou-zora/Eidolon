import esper
from common.engine.time import TimeUnit
from common.components.position import Position
from common.engine.processor import Processor
import logging

logger = logging.getLogger(__name__)


class LogProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, elapsed_time: TimeUnit) -> None:
        for ent, pos in esper.get_component(Position):
            logger.debug(f"Entity {ent}: {pos}")
