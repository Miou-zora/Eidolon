import logging

import esper

from common.components.leader import Leader
from common.components.physic_body import Physic
from common.components.position import Position
from common.components.velocity import Velocity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers.real_time_provider import RealTimeProvider

logger = logging.getLogger(__name__)


class FollowLeaderProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        time_provider = r.get_resource(RealTimeProvider)
        for ent, (lead, pos, vel) in esper.get_components(Leader, Position, Velocity):
            if lead.ent == -1 or not esper.has_component(lead.ent, Physic):
                continue
            leader_body: Physic = esper.component_for_entity(lead.ent, Physic)
            vel.x = (leader_body.body.position.x - pos.x) * lead.attraction
            vel.y = (leader_body.body.position.y - pos.y) * lead.attraction
