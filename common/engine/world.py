import esper

from .entity import EntityId
from .processor import Processor
from .resource_manager import ResourceManager
from .time import TimeUnit


class World:
    def __init__(self, name: str):
        self.name = name
        self.processors: list[Processor] = []

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(self, resource_manager: ResourceManager, elapsed_time: TimeUnit) -> None:
        for processor in self.processors:
            processor.process(resource_manager, elapsed_time)

    def add_processor(self, processor):
        self.processors.append(processor)
