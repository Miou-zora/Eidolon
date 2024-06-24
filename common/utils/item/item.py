from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from .meta_item import MetaItemId, MetaItem


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

    id: int
    meta_item_id: MetaItemId
    __last_id: ClassVar[int] = 0
    # current_durability
    # effects

    @classmethod
    def from_meta(cls, meta_item: MetaItem) -> Item:
        return cls(cls.__generate_id(), meta_item.id)

    @classmethod
    def __generate_id(cls) -> int:
        Item.__last_id += 1
        return Item.__last_id
