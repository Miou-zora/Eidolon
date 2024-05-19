import pyray

from resources.window_resource import WindowResource
from common.engine.engine import Engine
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager


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
