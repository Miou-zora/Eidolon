import logging

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers import UnitTimeProvider
from common.resources.time_providers.time_provider import TimeProvider

logger = logging.getLogger(__name__)


class RealTimeProviderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        time_provider: UnitTimeProvider = r.get_resource(TimeProvider)
        time_provider.update()
