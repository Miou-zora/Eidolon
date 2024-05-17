import logging

from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource import Resource
from common.engine.time import TimeUnit

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


class TestResource(Resource):
    def __init__(self):
        self.a = 0


def test_get_resource(dico, class_name: str):
    return dico[class_name]


class TestProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: dict[str, Resource], _: TimeUnit) -> None:
        test_resource: TestResource = test_get_resource(r, TestResource.__name__)
        test_resource.a += 1
        print(test_resource.a)


def run():
    engine: Engine = Engine()

    engine.register_resource(TestResource())
    engine.add_process(TestProcessor())

    entity: Entity = Entity()
    engine.run()


if __name__ == "__main__":
    run()
