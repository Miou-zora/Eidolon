import logging

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.physic_resource import PhysicResource

logger = logging.getLogger(__name__)


class PhysicProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager, elapsed_time: float) -> None:
        r.get_resource(PhysicResource).update(elapsed_time)
        # for ent, physic in esper.get_component(Physic):
        #     physic.body.velocity = (0, 0)
