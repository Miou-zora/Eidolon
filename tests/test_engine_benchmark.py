import random
import time

import esper
import pytest

from common.engine import component
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource import Resource
from common.engine.resource_manager import ResourceManager
from common.engine.schedule_label import ScheduleLabel


@pytest.mark.timeout(1)
def test_engine_benchmark_do_nothing():
    MAX_ITERATION_NUMBER = 8000000

    class DoNothingProcessor(Processor):
        current_iteration_number = 0

        def __init__(self, _engine: Engine):
            super().__init__()
            self.engine = _engine

        def process(self, r: ResourceManager) -> None:
            self.current_iteration_number += 1
            if self.current_iteration_number >= MAX_ITERATION_NUMBER:
                self.engine.stop()

    engine = Engine()
    engine.add_processors(ScheduleLabel.Update, DoNothingProcessor(engine))

    start_time = time.time()
    engine.run()
    end_time = time.time()

    print(
        f"\ntest_engine_benchmark_do_nothing: Time taken: {end_time - start_time} seconds",
        end="",
    )


@pytest.mark.timeout(1)
def test_engine_benchmark_access_resources():
    MAX_ITERATION_NUMBER = 5000000

    resource_class = [
        type(f"Resource{i}"), (Resource,), {"id": i}) for i in range(100)
    ]

    class ResourceAskerProcessor(Processor):
        current_iteration_number = 0

        def __init__(self, _engine: Engine):
            super().__init__()
            self.engine = _engine

        def process(self, r: ResourceManager) -> None:
            assert r.get_resource(resource_class[3]).id == 3
            self.current_iteration_number += 1
            if self.current_iteration_number >= MAX_ITERATION_NUMBER:
                self.engine.stop()

    engine = Engine()

    engine.insert_resources(*resource_class)
    engine.add_processors(ScheduleLabel.Update, ResourceAskerProcessor(engine))

    start_time = time.time()
    engine.run()
    end_time = time.time()

    print(
        f"\ntest_engine_benchmark_access_resources: Time taken: {end_time - start_time} seconds",
        end="",
    )


@pytest.mark.timeout(1)
def test_engine_benchmark_moving_entities():
    NUMBER_OF_ENTITIES = 10000
    MAX_ITERATION_NUMBER = 500

    @component
    class Position:
        x: int = 0
        y: int = 0

    class MoveProcessor(Processor):
        current_iteration_number = 0

        def __init__(self, _engine: Engine):
            super().__init__()
            self.engine = _engine

        def process(self, r: ResourceManager) -> None:
            for ent, pos in esper.get_component(Position):
                pos.x += 1
                pos.y += 1
            self.current_iteration_number += 1
            if self.current_iteration_number >= MAX_ITERATION_NUMBER:
                self.engine.stop()

    engine = Engine()

    for _ in range(NUMBER_OF_ENTITIES):
        Entity().add_components(Position())

    engine.add_processors(ScheduleLabel.Update, MoveProcessor(engine))

    start_time = time.time()
    engine.run()
    end_time = time.time()

    print(
        f"\ntest_engine_benchmark_moving_entities: Time taken: {end_time - start_time} seconds",
        end="",
    )


@pytest.mark.timeout(1)
def test_engine_benchmark_multiprocess():
    NUMBER_OF_ENTITIES = 10000
    MAX_ITERATION_NUMBER = 50

    @component
    class Position:
        x: int = 0
        y: int = 0

    @component
    class Velocity:
        x: int = 0
        y: int = 0

    class MoveProcessor(Processor):
        current_iteration_number = 0

        def __init__(self, _engine: Engine):
            super().__init__()
            self.engine = _engine

        def process(self, r: ResourceManager) -> None:
            for ent, (pos, vel) in esper.get_components(Position, Velocity):
                pos.x += vel.x
                pos.y += vel.y
            self.current_iteration_number += 1
            if self.current_iteration_number >= MAX_ITERATION_NUMBER:
                self.engine.stop()

    class VeloProcessor(Processor):
        def process(self, r: ResourceManager) -> None:
            for ent, vel in esper.get_component(Velocity):
                vel.x += random.randint(-1, 1)
                vel.y += random.randint(-1, 1)

    engine = Engine()

    for e in range(NUMBER_OF_ENTITIES):
        Entity().add_components(Position(), Velocity())

    engine.add_processors(
        ScheduleLabel.Update,
        VeloProcessor(),
        MoveProcessor(engine),
    )

    start_time = time.time()
    engine.run()
    end_time = time.time()

    print(
        f"\ntest_engine_benchmark_multiprocess: Time taken: {end_time - start_time} seconds",
        end="",
    )
