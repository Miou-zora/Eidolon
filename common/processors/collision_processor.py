import logging

import esper

from common.components.box_collider import BoxCollider
from common.components.name import Name
from common.components.position import Position
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager

logger = logging.getLogger(__name__)


class CollisionProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        for ent_ori, (box_ori, pos_ori) in esper.get_components(BoxCollider, Position):
            for ent_dest, (box_dest, pos_dest) in esper.get_components(
                BoxCollider, Position
            ):
                if ent_ori == ent_dest:
                    continue
                if self.collide(box_ori, pos_ori, box_dest, pos_dest):
                    ent_ori_name = esper.component_for_entity(ent_ori, Name).name
                    ent_dest_name = esper.component_for_entity(ent_dest, Name).name
                    logger.info(
                        f"Collision detected between {ent_ori_name} and {ent_dest_name}"
                    )

    @staticmethod
    def collide(
        box1: BoxCollider, pos1: Position, box2: BoxCollider, pos2: Position
    ) -> bool:
        return (
            pos1.x < pos2.x + box2.x
            and pos1.x + box1.x > pos2.x
            and pos1.y < pos2.y + box2.y
            and pos1.y + box1.y > pos2.y
        )
