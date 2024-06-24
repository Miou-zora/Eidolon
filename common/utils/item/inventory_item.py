from common.utils.vector2 import Vector2
from .item import Item


class InventoryItem(Item):
    """
    InventoryItem is an item with more infos like:
    - Position in the inventory
    - Favorite status
    - Quantity
    """

    position: Vector2
    # favorite
    # quantity
