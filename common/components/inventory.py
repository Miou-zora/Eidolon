from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from common.engine import component
from common.utils.item.inventory_item import InventoryItem
from common.utils.vector2 import Vector2

if TYPE_CHECKING:
    from typing import Callable


@component
class Inventory:
    __items: list[Optional[InventoryItem]]
    __size: Vector2

    def __init__(self, size: Vector2):
        self.__size = size
        self.__items = [None] * int(size.x * size.y)

    @staticmethod
    def __check_cords(fn) -> Callable:
        def wrapper(self, x: int, y: int, *args, **kwargs):
            if not (0 <= x < self.__size.x and 0 <= y < self.__size.y):
                return None
            return fn(self, x, y, *args, **kwargs)

        return wrapper

    @__check_cords
    def add_item(self, x: int, y: int, item: InventoryItem) -> Optional[InventoryItem]:
        if self.get_item(x, y) is not None:
            item_before = self.get_item(x, y)
            self.__items[int(x + y * self.__size.x)] = item
            return item_before
        else:
            self.__items[int(x + y * self.__size.x)] = item

    @__check_cords
    def get_item(self, x: int, y: int) -> Optional[InventoryItem]:
        return self.__items[int(x + y * self.__size.x)]

    def get_size(self) -> Vector2:
        return self.__size

    @__check_cords
    def remove_item(self, x: int, y: int) -> Optional[InventoryItem]:
        item = self.__items[int(x + y * self.__size.x)]
        self.__items[int(x + y * self.__size.x)] = None
        return item

    def __str__(self) -> str:
        return f"InventoryItem({len(self.__items)} items)"
