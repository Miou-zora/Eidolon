import logging

import esper

from common.components.box_collider import BoxCollider
from common.components.collisions import Collisions, CollisionDirection
from common.components.groundable import Groundable
from common.components.position import Position
from common.components.static_body import StaticBody
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager

logger = logging.getLogger(__name__)


class PhysicProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        for ent, (pos, collisions, collider) in esper.get_components(
            Position, Collisions, BoxCollider
        ):
            for collision in collisions.collisions_between_entity:
                collided_ent = collision.entity
                if not esper.has_component(collided_ent, StaticBody):
                    continue
                collided_pos = esper.component_for_entity(collided_ent, Position)
                collided_collider = esper.component_for_entity(
                    collided_ent, BoxCollider
                )
                if collision.direction == CollisionDirection.LEFT:
                    pos.x = collided_pos.x + collided_collider.x
                elif collision.direction == CollisionDirection.RIGHT:
                    pos.x = collided_pos.x - collider.x
                elif collision.direction == CollisionDirection.UP:
                    pos.y = collided_pos.y + collided_collider.y
                else:
                    pos.y = collided_pos.y - collider.y
                    if esper.has_component(ent, Groundable):
                        esper.component_for_entity(ent, Groundable).grounded = True
