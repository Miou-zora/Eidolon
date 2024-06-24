from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine.resource import Resource

if TYPE_CHECKING:
    from typing import Optional
    from common.engine.engine import Engine
    from common.utils.item.meta_item import MetaItem, MetaItemId


class MetaItemManager(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.__meta_items: dict[MetaItemId, MetaItem] = {}

    def register_meta_item(self, meta_item: MetaItem) -> None:
        if meta_item.id in self.__meta_items:
            raise ValueError(f"MetaItem with id {meta_item.id} already exists")
        self.__meta_items[meta_item.id] = meta_item

    def generate_meta_item_id(self) -> MetaItemId:
        return max(self.__meta_items.keys(), default=0) + 1

    def get_meta_item(self, meta_item_id: MetaItemId) -> Optional[MetaItem]:
        return self.__meta_items.get(meta_item_id, None)
