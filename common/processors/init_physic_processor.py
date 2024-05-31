import logging

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.physic_resource import PhysicResource

logger = logging.getLogger(__name__)


class InitPhysicProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        world = r.get_resource(PhysicResource)
        world.world.gravity = (0, 900)
