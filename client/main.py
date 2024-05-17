import logging
from typing import Any, TypeVar

import esper
from dataclasses import dataclass as component
from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

type Component = Any
type TimeUnit = int
type EntityId = int
Processor = esper.Processor
ProcessorClass = TypeVar("ProcessorClass", bound=Processor)


@component
class Position:
    x: float = 0.0
    y: float = 0.0

    def __str__(self) -> str:
        return f"Position({self.x},{self.y})"


class LogProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, elapsed_time: TimeUnit) -> None:
        for ent, pos in esper.get_component(Position):
            logger.debug(f"Entity {ent}: {pos}")


class Entity:
    def __init__(self):
        self.id: EntityId = esper.create_entity()

    def add_component(self, component_instance: Any) -> None:
        esper.add_component(self.id, component_instance)


class World:
    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def create_entity() -> EntityId:
        return esper.create_entity()

    def update(self, elapsed_time: TimeUnit) -> None:
        esper.process(elapsed_time)


class TimeProvider(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def get_elapsed_time(self) -> TimeUnit:
        return 1


class UnitTimeProvider(TimeProvider):
    def __init__(self, unit: TimeUnit = 1):
        self._unit: TimeUnit = unit

    def update(self) -> None:
        pass

    def get_elapsed_time(self) -> TimeUnit:
        return self._unit


class Engine:
    def __init__(self, time_provider: TimeProvider | None = None):
        self._running = False
        self.world: World = World(esper.current_world)
        if time_provider is None:
            self.time_provider = UnitTimeProvider()
        else:
            self.time_provider: TimeProvider = time_provider

    def run(self) -> None:
        self._running = True
        while self._running:
            self.time_provider.update()
            self.world.update(self.time_provider.get_elapsed_time())

    def add_process(self, processor: ProcessorClass) -> None:
        esper.add_processor(processor)


def run():
    engine: Engine = Engine()
    engine.add_process(LogProcessor())
    entity: Entity = Entity()
    entity.add_component(Position(1, 1))
    engine.run()


if __name__ == "__main__":
    run()
