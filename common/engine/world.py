from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import esper

from .schedule_label import ScheduleLabel

if TYPE_CHECKING:
    from typing import Type, TypeVar

    from .entity import EntityId
    from .processor import Processor
    from .resource_manager import ResourceManager

    RM = TypeVar("RM", bound=ResourceManager)

logger = logging.getLogger(__name__)


class World:

    def __init__(self, name: str):
        self.name = name
        self.processors: dict[ScheduleLabel, list[Type[Processor]]] = {
            label: [] for label in ScheduleLabel
        }

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(
        self, schedule: ScheduleLabel, resource_manager: RM, *args, **kargs
    ) -> None:
        esper.clear_dead_entities()
        for processor in self.processors[schedule]:
            processor.process(resource_manager, *args, **kargs)

    def add_processor(
        self, schedule: ScheduleLabel, processor: Type[Processor]
    ) -> None:
        self.processors[schedule].append(processor)
