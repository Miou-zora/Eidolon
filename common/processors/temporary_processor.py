import logging

import esper

from common.components.name import Name
from common.components.temporary import Temporary
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers.real_time_provider import RealTimeProvider

logger = logging.getLogger(__name__)


class TemporaryProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        elapsed_time = r.get_resource(RealTimeProvider).get_elapsed_time()
        for ent, temp in esper.get_component(Temporary):
            temp.elapsed += elapsed_time
            if temp.elapsed >= temp.duration:
                logger.debug(
                    "Entity %s has expired",
                    (
                        esper.component_for_entity(ent, Name)
                        if esper.has_component(ent, Name)
                        else ent
                    ),
                )
                esper.delete_entity(ent)
