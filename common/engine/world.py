import esper

from .entity import EntityId
from .processor import ProcessorClass
from .resource_manager import ResourceManager


class World:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(self, resource_manager: ResourceManager) -> None:
        esper.process(resource_manager)

    def add_processor(self, processor: ProcessorClass) -> None:
        esper.add_processor(processor)
