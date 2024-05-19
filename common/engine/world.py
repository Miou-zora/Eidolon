from typing import Type

import esper

from .entity import EntityId
from .processor import Processor
from .resource_manager import ResourceManager
from .schedule_label import ScheduleLabel


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
        self, schedule: ScheduleLabel, resource_manager: ResourceManager
    ) -> None:
        esper.clear_dead_entities()
        for processor in self.processors[schedule]:
            processor.process(resource_manager)

    def add_processor(
        self, schedule: ScheduleLabel, processor: Type[Processor]
    ) -> None:
        self.processors[schedule].append(processor)
