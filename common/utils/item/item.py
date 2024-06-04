from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from .meta_item import MetaItemId, MetaItem

if TYPE_CHECKING:
    ItemId = int

item_id = 0


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

    id: ItemId
    meta_item_id: MetaItemId
    # current_durability
    # effects

    @classmethod
    def create_from_meta_item(cls, meta_item: MetaItem) -> Item:
        return cls(cls.__generate_id(), meta_item.id)

    @classmethod
    def __generate_id(cls) -> ItemId:
        global item_id
        item_id += 1
        return item_id

    def __str__(self):
        return f"Item({self.meta_item_id})"
