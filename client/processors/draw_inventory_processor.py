import logging

import esper
import pyray as raylib

from common.components.inventory import Inventory
from common.components.name import Name
from common.components.position import Position
from common.engine import Processor
from common.engine.entity import Entity
from common.engine.resource_manager import ResourceManager
from common.resources.meta_item_manager import MetaItemManager
from components.draw_inventory import DrawInventory
from components.drawable import Drawable
from resources.inputs_manager import InputsManager

logger = logging.getLogger(__name__)


class DrawInventoryProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        inputs_manager = r.get_resource(InputsManager)
        meta_item_manager = r.get_resource(MetaItemManager)
        space_pressed = InputsManager.is_key_pressed(raylib.KeyboardKey.KEY_SPACE)
        if not space_pressed:
            return
        for ent, inv in esper.get_component(Inventory):
            if esper.has_component(ent, DrawInventory):
                draw_in = esper.remove_component(ent, DrawInventory)
                for item in draw_in.items:
                    esper.delete_entity(item)
            else:
                draw_in = DrawInventory()
                esper.add_component(ent, draw_in)
                for y in range(int(inv.get_size().y)):
                    for x in range(int(inv.get_size().x)):
                        if inv.get_item(x, y) is None:
                            continue
                        item = inv.get_item(x, y)
                        meta_item = meta_item_manager.get_meta_item(item.meta_item_id)
                        if meta_item is None:
                            continue
                        draw_in.items.append(
                            Entity()
                            .add_components(
                                Position.from_size(x * 30, y * 30),
                                Drawable(meta_item.sprite, 10, 1),  # 1 is UI_CAM_ID
                                Name(item.__str__()),
                            )
                            .id
                        )
