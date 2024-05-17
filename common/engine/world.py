import esper

from common.engine.entity import EntityId
from common.engine.time import TimeUnit


class World:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(self, elapsed_time: TimeUnit) -> None:
        esper.process(elapsed_time)
