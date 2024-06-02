import logging
from itertools import combinations

import esper

from common.components.box_collider import BoxCollider
from common.components.collision_mask import CollisionMask
from common.components.collisions import (
    Collisions, Collision, CollisionDirection
)
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.utils.vector2 import Vector2

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
            self.create_collision(
                iter_ent, pos, iter_pos, collider, iter_collider, collisions
            )

    @staticmethod
    def create_collision(
        iter_ent: int,
        pos: Position,
        iter_pos: Position,
        collider: BoxCollider,
        iter_collider: BoxCollider,
        collisions: Collisions,
    ) -> None:
        box = CollisionProcessor.get_box(pos, collider)
        old_box = CollisionProcessor.get_box(collisions.last_position, collider)

        collided_from_left = old_box["right"] <= iter_pos.x < box["right"]
        collided_from_right = (
            old_box["left"] >= iter_pos.x + iter_collider.x > box["left"]
        )
        collided_from_top = old_box["bottom"] <= iter_pos.y < box["bottom"]
        collided_from_bottom = (
            old_box["top"] >= iter_pos.y + iter_collider.y > box["top"]
        )

        collisions_possibility = [
            (collided_from_top, CollisionDirection.DOWN),
            (collided_from_bottom, CollisionDirection.UP),
            (collided_from_right, CollisionDirection.LEFT),
            (collided_from_left, CollisionDirection.RIGHT),
        ]
        for collided in collisions_possibility:
            if collided[0]:
                collisions.collisions_between_entity.append(
                    Collision(iter_ent, collided[1])
                )
                break

    @staticmethod
    def get_box(pos: Vector2 | Position, collider: BoxCollider) -> dict[str, float]:
        return {
            "left": pos.x,
            "right": pos.x + collider.x,
            "top": pos.y,
            "bottom": pos.y + collider.y,
        }

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
