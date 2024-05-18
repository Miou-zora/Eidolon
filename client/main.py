import logging

from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.processors.log_processor import LogProcessor
from common.resources.time_providers import UnitTimeProvider

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


def run():
    engine: Engine = Engine()

    engine.register_resource(UnitTimeProvider())
    engine.add_processor(LogProcessor())

    entity: Entity = Entity()
    entity.add_component(Position(32, 64))
    entity.add_component(Name("First Entity"))
    entity2: Entity = Entity()
    entity2.add_component(Position(69, 42))
    entity2.add_component(Name("Second Entity"))

    engine.run()


if __name__ == "__main__":
    run()
