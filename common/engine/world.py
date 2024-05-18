import esper

from .entity import EntityId
from .processor import ProcessorClass
from .resource_manager import ResourceManager
from .time import TimeUnit


class World:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(self, resource_manager: ResourceManager, elapsed_time: TimeUnit) -> None:
        esper.process(resource_manager, elapsed_time)

    def add_processor(self, processor: ProcessorClass) -> None:
        esper.add_processor(processor)
