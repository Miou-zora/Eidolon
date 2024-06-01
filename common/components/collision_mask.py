from __future__ import annotations

from common.engine import component


@component
class CollisionMask:
    """
    Layer corresponds on which layer the entity is.
    """

    layer: int
    """
    It corresponds to the layers that the entity can collide with.
    """
    mask: int

    @staticmethod
    def a_can_collide_b(mask_a: CollisionMask, mask_b: CollisionMask) -> bool:
        return (mask_a.mask & mask_b.layer) != 0
