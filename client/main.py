import logging

import pyray

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


class WindowResource(Resource):
    def __init__(
        self, width: int = 1680, height: int = 1050, title: str = "Eidolon Engine"
    ):
        pyray.init_window(width, height, title)


class WindowProcessor(Processor):
    def __init__(self, engine: Engine):
        super().__init__()
        self.engine: Engine = engine

    def process(self, r: ResourceManager) -> None:
        window_resource: WindowResource = r.get_resource(WindowResource)
        if window_resource is None:
            raise NotImplemented(
                f"Resource not found: WindowResource:{window_resource}"
            )
        if pyray.window_should_close():
            pyray.close_window()
            self.engine.stop()


class DrawProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        pyray.draw_text(
            "Congrats! You created your first window!", 190, 200, 20, pyray.LIGHTGRAY
        )
        pyray.end_drawing()


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
    engine.register_resource(WindowResource())
    engine.add_processor(WindowProcessor(engine))
    engine.add_processor(DrawProcessor())
    engine.add_processor(TestProcessor())

    Entity()
    engine.run()


if __name__ == "__main__":
    run()
