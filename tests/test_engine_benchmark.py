import os
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


def no_checked_by_ci(fn):
    if "CI" in os.environ:
        return pytest.mark.skip(reason="Not checked by CI")(fn)
    return fn


def time_report(fn):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        fn(*args, **kwargs)
        end_time = time.time()
        print(f"\n{fn.__name__} Time taken: {end_time - start_time} seconds", end="")

    return wrapper


@no_checked_by_ci
@pytest.mark.timeout(1)
@time_report
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

    engine.run()


@no_checked_by_ci
@pytest.mark.timeout(1)
@time_report
def test_engine_benchmark_access_resources():
    MAX_ITERATION_NUMBER = 3000000

    resource_class = [type(f"Resource{i}", (Resource,), {"id": i}) for i in range(100)]

    class ResourceAskerProcessor(Processor):
        current_iteration_number = 0

        def __init__(self, _engine: Engine):
            super().__init__()
            self.engine = _engine

        def process(self, r: ResourceManager) -> None:
            random_resource_index = 99
            assert (
                r.get_resource(resource_class[random_resource_index]).id
                == random_resource_index
            )
            self.current_iteration_number += 1
            if self.current_iteration_number >= MAX_ITERATION_NUMBER:
                self.engine.stop()

    engine = Engine()

    engine.insert_resources(*resource_class)
    engine.add_processors(ScheduleLabel.Update, ResourceAskerProcessor(engine))

    engine.run()


@no_checked_by_ci
@pytest.mark.timeout(1)
@time_report
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

    engine.run()


@no_checked_by_ci
@pytest.mark.timeout(1)
@time_report
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

    engine.run()
