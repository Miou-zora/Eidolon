import logging

from client.processors.render_processor import RenderProcessor
from client.processors.window_processor import WindowProcessor
from client.resources.window_resource import WindowResource
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource import Resource
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers import UnitTimeProvider
from common.resources.time_providers.time_provider import TimeProvider

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


class TestResource(Resource):
    def __init__(self):
        self.a = 0


class TestProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        test_resource: TestResource = r.get_resource(TestResource)
        time_provider: UnitTimeProvider = r.get_resource(TimeProvider)
        if test_resource is None or time_provider is None:
            raise NotImplemented(
                f"Resource not found: TestResource:{test_resource} or UnitTimeProvider:{time_provider}"
            )
        test_resource.a += 1


def run():
    engine: Engine = Engine()

    engine.register_resource(TestResource())
    engine.register_resource(UnitTimeProvider())
    engine.register_resource(WindowResource(title="Eidolon"))
    engine.add_processor(WindowProcessor(engine))
    engine.add_processor(RenderProcessor())
    engine.add_processor(TestProcessor())

    Entity()
    engine.run()


if __name__ == "__main__":
    run()
