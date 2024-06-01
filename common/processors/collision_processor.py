import logging

import esper

from common.components.box_collider import BoxCollider
from common.components.collision_mask import CollisionMask
from common.components.collisions import Collisions, Collision
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager

logger = logging.getLogger(__name__)


class CollisionProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        for ent, (pos, collisions, collision_mask, collider) in esper.get_components(
            Position, Collisions, CollisionMask, BoxCollider
        ):
            collisions.collisions_between_entity = []
            for iter_ent, (
                iter_collision_mask,
                iter_pos,
                iter_box_collider,
            ) in esper.get_components(CollisionMask, Position, BoxCollider):
                if ent == iter_ent:
                    continue
                if not CollisionMask.a_can_collide_b(
                    collision_mask, iter_collision_mask
                ):
                    continue
                if not CollisionProcessor.aabb_collision(
                    pos, collider, iter_pos, iter_box_collider
                ):
                    continue
                boxleft = pos.x
                boxright = pos.x + collider.x
                boxtop = pos.y
                boxbottom = pos.y + collider.y
                oldBoxLeft = collisions.last_position.x
                oldBoxRight = collisions.last_position.x + collider.x
                oldBoxTop = collisions.last_position.y
                oldBoxBottom = collisions.last_position.y + collider.y

                collidedFromLeft = oldBoxRight <= iter_pos.x < boxright
                collidedFromRight = (
                    oldBoxLeft >= iter_pos.x + iter_box_collider.x > boxleft
                )
                collidedFromTop = oldBoxBottom <= iter_pos.y < boxbottom
                collidedFromBottom = (
                    oldBoxTop >= iter_pos.y + iter_box_collider.y > boxtop
                )
                if collidedFromTop:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.DOWN)
                    )
                elif collidedFromBottom:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.UP)
                    )
                elif collidedFromLeft:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.RIGHT)
                    )
                elif collidedFromRight:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.LEFT)
                    )

                if len(collisions.collisions_between_entity) > 0:
                    logger.debug(
                        f"Entity {ent} collided with {iter_ent} in directions {collisions.collisions_between_entity}"
                    )

    @staticmethod
    def aabb_collision(
        pos1: Position,
        collider1: BoxCollider,
        pos2: Position,
        collider2: BoxCollider,
    ) -> bool:
        return (
            pos1.x < pos2.x + collider2.x
            and pos1.x + collider1.x > pos2.x
            and pos1.y < pos2.y + collider2.y
            and pos1.y + collider1.y > pos2.y
        )
