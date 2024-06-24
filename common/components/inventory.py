from __future__ import annotations

from dataclasses import field
from functools import wraps
from typing import Optional, TYPE_CHECKING

from common.engine import component
from common.utils.item.inventory_item import InventoryItem
from common.utils.vector2 import Vector2

if TYPE_CHECKING:
    from typing import Protocol, TypeVar

    T = TypeVar("T")


    class CheckCordMethod(Protocol):
        # inv_instance == self in the Inventory class
        def __call__(
            self, inv_instance: Inventory, x: int, y: int, *args, **kwargs
        ) -> T: ...


@component
class Inventory:
    __size: Vector2
    __items: list[Optional[InventoryItem]] = field(default_factory=list)

    def __post_init__(self):
        self.__items = [None] * int(self.size.x * self.size.y)

    @staticmethod
    def __check_cords(fn: CheckCordMethod) -> CheckCordMethod:
        @wraps(fn)
        def wrapper(self, x: int, y: int, *args, **kwargs) -> T:
            if not (0 <= x < self.size.x and 0 <= y < self.size.y):
                return None
            return fn(self, x, y, *args, **kwargs)

        return wrapper

    @__check_cords
    def add_item(self, x: int, y: int, item: InventoryItem) -> Optional[
        InventoryItem]:
        item_before = self.get_item(x, y)
        self.__items[int(x + y * self.size.x)] = item
        return item_before

    @__check_cords
    def get_item(self, x: int, y: int) -> Optional[InventoryItem]:
        return self.__items[int(x + y * self.size.x)]

    @property
    def size(self) -> Vector2:
        return self.__size

    @__check_cords
    def remove_item(self, x: int, y: int) -> Optional[InventoryItem]:
        item = self.__items[int(x + y * self.size.x)]
        self.__items[int(x + y * self.size.x)] = None
        return item

    def __str__(self) -> str:
        return f"InventoryItem({len(self.__items)} items)"
