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

    def collide_with(self, mask_b: CollisionMask) -> bool:
        return self.mask & mask_b.layer
