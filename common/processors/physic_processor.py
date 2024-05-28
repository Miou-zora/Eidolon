import logging

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.physic_resource import PhysicResource
from common.resources.time_providers.real_time_provider import RealTimeProvider

logger = logging.getLogger(__name__)


class PhysicProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.max_chrono_value = 1 / 60
        self.current_chrono_value = 0

    def process(self, r: ResourceManager) -> None:
        world = r.get_resource(PhysicResource)
        time_provider = r.get_resource(RealTimeProvider)
        self.current_chrono_value += time_provider.get_elapsed_time()
        if self.current_chrono_value >= self.max_chrono_value:
            self.current_chrono_value -= self.max_chrono_value
            world.update(self.max_chrono_value)
