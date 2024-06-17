import itertools
import logging

import esper
import pyray as raylib

from common.components.inventory import Inventory
from common.components.name import Name
from common.components.position import Position
from common.engine import Processor
from common.engine.entity import Entity
from common.engine.entity import EntityId
from common.engine.resource_manager import ResourceManager
from common.resources.meta_item_manager import MetaItemManager
from components.draw_inventory import DrawInventory
from components.drawable import Drawable
from components.main_player_tag import MainPlayerTag
from resources.inputs_manager import InputsManager

logger = logging.getLogger(__name__)


class DrawInventoryProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        if not r.get_resource(InputsManager).is_key_pressed(
            raylib.KeyboardKey.KEY_SPACE
        ):
            return
        for ent, (inv, _) in esper.get_components(Inventory, MainPlayerTag):
            if esper.has_component(ent, DrawInventory):
                DrawInventoryProcessor.close_inventory(ent)
            else:
                DrawInventoryProcessor.open_inventory(
                    ent, inv, r.get_resource(MetaItemManager)
                )

    @staticmethod
    def close_inventory(ent: EntityId) -> None:
        draw_in = esper.remove_component(ent, DrawInventory)
        for item in draw_in.items:
            esper.delete_entity(item)

    @staticmethod
    def open_inventory(
        ent: EntityId, inv: Inventory, meta_item_manager: MetaItemManager
    ) -> None:
        draw_in = DrawInventory()
        esper.add_component(ent, draw_in)
        width, height = inv.get_size().x, inv.get_size().y
        for x, y in itertools.product(range(int(width)), range(int(height))):
            if inv.get_item(x, y) is None:
                continue
            item = inv.get_item(x, y)
            if item is None:
                continue
            meta_item = meta_item_manager.get_meta_item(item.meta_item_id)
            if meta_item is None:
                continue
            draw_in.items.append(
                Entity()
                .add_components(
                    Position.from_size(100 + x * 40, 100 + y * 40),
                    Drawable(meta_item.sprite, 11, 1),
                    # 1 is UI_CAM_ID
                    Name(str(item)),
                )
                .id
            )
