import logging
from typing import Any

import esper
from dataclasses import dataclass as component
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


@component
class Position:
    x: float = 0.0
    y: float = 0.0

    def __str__(self) -> str:
        return f"Position({self.x},{self.y})"


type Component = Any
type TimeType = int


class LogProcessor(esper.Processor):
    def __init__(self):
        super().__init__()

    def process(self, elapsed_time):
        for ent, pos in esper.get_component(Position):
            logger.debug(f"Entity {ent}: {pos}")


class Entity:
    def __init__(self):
        self.id = esper.create_entity()

    def add_component(self, component_instance: Any):
        esper.add_component(self.id, component_instance)


class World:
    def __init__(self, name: str):
        self.name = str

    @staticmethod
    def create_entity():
        return esper.create_entity()


class TimeProvider(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get_elapsed_time(self) -> TimeType:
        return 1


class UnitTimeProvider(TimeProvider):
    def __init__(self, unit: TimeType = 1):
        self._unit: TimeType = unit

    def update(self):
        pass

    def get_elapsed_time(self) -> TimeType:
        return self._unit


class Engine:
    def __init__(self, time_provider=UnitTimeProvider()):
        self._running = False
        self.world: World = World(esper.current_world)
        self.time_provider: TimeProvider = time_provider

    def run(self):
        self._running = True
        while self._running:
            self.time_provider.update()
            self.update(self.time_provider.get_elapsed_time())

    def update(self, elapsed_time: TimeType):
        esper.process(elapsed_time)

    def add_process(self, processor):
        esper.add_processor(processor())


def run():
    engine: Engine = Engine()
    engine.add_process(LogProcessor)
    entity: Entity = Entity()
    entity.add_component(Position(1, 1))
    engine.run()


if __name__ == "__main__":
    run()
