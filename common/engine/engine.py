import esper

from common.engine.processor import ProcessorClass
from common.engine.time_provider import TimeProvider
from common.engine.world import World

# Ugly
from common.utils.time_providers.unit_time_provider import UnitTimeProvider


class Engine:
    def __init__(self, time_provider: TimeProvider | None = None):
        self._running = False
        self.world: World = World(esper.current_world)
        if time_provider is None:
            self.time_provider = UnitTimeProvider()
        else:
            self.time_provider = time_provider

    def run(self) -> None:
        self._running = True
        while self._running:
            self.time_provider.update()
            self.world.update(self.time_provider.get_elapsed_time())

    def add_process(self, processor: ProcessorClass) -> None:
        esper.add_processor(processor)
