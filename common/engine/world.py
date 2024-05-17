import esper

from .entity import EntityId
from .resource import Resource
from .time import TimeUnit


class World:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(self, resources: dict[str, Resource], elapsed_time: TimeUnit) -> None:
        esper.process(resources, elapsed_time)
