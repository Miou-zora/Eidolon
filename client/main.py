import logging

from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.processors.log_processor import LogProcessor

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


def run():
    engine: Engine = Engine()
    engine.add_process(LogProcessor())
    entity: Entity = Entity()
    entity.add_component(Position(1, 1))
    engine.run()


if __name__ == "__main__":
    run()
