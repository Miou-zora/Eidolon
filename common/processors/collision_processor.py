import logging
from itertools import combinations

import esper

from common.components.box_collider import BoxCollider
from common.components.collision_mask import CollisionMask
from common.components.collisions import Collisions, Collision, \
    CollisionDirection
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager

logger = logging.getLogger(__name__)


class CollisionProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        for (
            (ent, (pos, collision_mask, collider)),
            (iter_ent, (iter_pos, iter_collision_mask, iter_collider)),
        ) in combinations(
            esper.get_components(Position, CollisionMask, BoxCollider), 2
        ):
            if not esper.has_component(ent, Collisions):
                continue
            collisions = esper.component_for_entity(ent, Collisions)
            collisions.collisions_between_entity.clear()
            if ent == iter_ent:
                continue
            if not collision_mask.collide_with(iter_collision_mask):
                continue
            if not CollisionProcessor.aabb_collision(
                pos, collider, iter_pos, iter_collider
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
                old_box_left >= iter_pos.x + iter_collider.x > box_left
            )
            collided_from_top = old_box_bottom <= iter_pos.y < box_bottom
            collided_from_bottom = old_box_top >= iter_pos.y + iter_collider.y > box_top
            if collided_from_top:
                collisions.collisions_between_entity.append(
                    Collision(iter_ent, CollisionDirection.DOWN)
                )
            elif collided_from_bottom:
                collisions.collisions_between_entity.append(
                    Collision(iter_ent, CollisionDirection.UP)
                )
            elif collided_from_left:
                collisions.collisions_between_entity.append(
                    Collision(iter_ent, CollisionDirection.RIGHT)
                )
            elif collided_from_right:
                collisions.collisions_between_entity.append(
                    Collision(iter_ent, CollisionDirection.LEFT)
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
