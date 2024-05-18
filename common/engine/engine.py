import esper

# Ugly
from common.utils.time_providers.unit_time_provider import UnitTimeProvider
from .processor import ProcessorClass
from .resource import Resource
from .resource_manager import ResourceManager
from .time_provider import TimeProvider
from .world import World


class Engine:
    def __init__(self, time_provider: TimeProvider | None = None):
        self._running = False
        self.world: World = World(esper.current_world)
        # TODO: add time provider to resource manager
        if time_provider is None:
            self.time_provider = UnitTimeProvider()
        else:
            self.time_provider = time_provider
        self.resource_manager: ResourceManager = ResourceManager()

    def run(self) -> None:
        self._running = True
        while self._running:
            self.time_provider.update()
            self.world.update(
                self.resource_manager, self.time_provider.get_elapsed_time()
            )

    def register_resource(self, resource: Resource) -> None:
        self.resource_manager.add_resource(resource)

    def add_processor(self, processor: ProcessorClass) -> None:
        self.world.add_processor(processor)
