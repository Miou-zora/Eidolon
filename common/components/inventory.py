from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from common.engine import component
from common.utils.vector2 import Vector2

if TYPE_CHECKING:
    MetaItemId = int


@dataclass
class MetaItem:
    """
    MetaItem should be used to give various infos about an item like:
    - Name
    - Description
    - Pattern (MetaItems to use to craft this item)
    - Possible effects
    - Durability
    - Sprite
    - Is stackable
    - ID
    These infos are just examples and can be changed.
    """

    name: str
    # description
    # pattern
    # effects
    # durability
    sprite: str
    # is_stackable
    id: MetaItemId


@dataclass
class Item:
    """
    Items are the actual objects that can be stored.
    It contains various infos about the concrete item like:
    - MetaItemId
    - CurrentDurability
    - Specific effects with their values
    These infos are just examples and can be changed.
    """

    meta_item_id: MetaItemId
    # current_durability
    # effects


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


@component
class DrawInventory:
    """
    Tag to know inventory should be drawn
    """

    pass


@component
class Inventory:
    __items: list[Optional[InventoryItem]]
    __size: Vector2

    def __init__(self, size: Vector2):
        self.__size = size
        self.__items = [None] * int(size.x * size.y)

    @staticmethod
    def __check_cords(fn: callable) -> callable:
        def wrapper(self, x: int, y: int, *args, **kwargs) -> None:
            if not (0 <= x < self.__size.x and 0 <= y < self.__size.y):
                return
            return fn(self, x, y, *args, **kwargs)

        return wrapper

    @__check_cords
    def add_item(self, x: int, y: int, item: InventoryItem) -> None:
        self.__items[int(x + y * self.__size.x)] = item

    @__check_cords
    def get_item(self, x: int, y: int) -> Optional[InventoryItem]:
        return self.__items[int(x + y * self.__size.x)]

    @__check_cords
    def remove_item(self, x: int, y: int) -> Optional[InventoryItem]:
        item = self.__items[int(x + y * self.__size.x)]
        self.__items[int(x + y * self.__size.x)] = None
        return item

    def __str__(self) -> str:
        return f"InventoryItem({len(self.__items)} items)"
