import esper

# Ugly
from common.utils.time_providers.unit_time_provider import UnitTimeProvider
from .processor import ProcessorClass
from .resource import Resource
from .time_provider import TimeProvider
from .world import World


class Engine:
    def __init__(self, time_provider: TimeProvider | None = None):
        self._running = False
        self.world: World = World(esper.current_world)
        if time_provider is None:
            self.time_provider = UnitTimeProvider()
        else:
            self.time_provider = time_provider
        self.resources: dict[str, Resource] = dict()

    def run(self) -> None:
        self._running = True
        while self._running:
            self.time_provider.update()
            self.world.update(self.resources, self.time_provider.get_elapsed_time())

    def register_resource(self, resource: Resource) -> None:
        self.resources[resource.__class__.__name__] = resource

    def add_process(self, processor: ProcessorClass) -> None:
        esper.add_processor(processor)
