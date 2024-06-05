from __future__ import annotations

from common.engine import component


@component
class CollisionMask:
    """
    Helper class to filter out collisions based on layer mask
    
    Attributes
    ----------
    layer: int
        Layer corresponds on which layer the entity is.

    mask: int
        It corresponds to the layers that the entity can collide with.
    """

    layer: int
    mask: int

    def collide_with(self, mask_b: CollisionMask) -> bool:
        return self.mask & mask_b.layer
