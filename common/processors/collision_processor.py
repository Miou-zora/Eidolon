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
                box_left = pos.x
                box_right = pos.x + collider.x
                box_top = pos.y
                box_bottom = pos.y + collider.y
                old_box_left = collisions.last_position.x
                old_box_right = collisions.last_position.x + collider.x
                old_box_top = collisions.last_position.y
                old_box_bottom = collisions.last_position.y + collider.y

                collided_from_left = old_box_right <= iter_pos.x < box_right
                collided_from_right = (
                    old_box_left >= iter_pos.x + iter_box_collider.x > box_left
                )
                collided_from_top = old_box_bottom <= iter_pos.y < box_bottom
                collided_from_bottom = (
                    old_box_top >= iter_pos.y + iter_box_collider.y > box_top
                )
                if collided_from_top:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.DOWN)
                    )
                elif collided_from_bottom:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.UP)
                    )
                elif collided_from_left:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.RIGHT)
                    )
                elif collided_from_right:
                    collisions.collisions_between_entity.append(
                        Collision(iter_ent, Collision.Direction.LEFT)
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
