import logging

import pyray as raylib

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager

logger = logging.getLogger(__name__)


class EndDrawingProcessor(Processor):
    def process(self, _: ResourceManager) -> None:
        raylib.end_drawing()
