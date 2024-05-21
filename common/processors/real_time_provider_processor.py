import logging

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers.real_time_provider import RealTimeProvider

logger = logging.getLogger(__name__)


class RealTimeProviderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        time_provider = r.get_resource(RealTimeProvider)
        time_provider.update()
