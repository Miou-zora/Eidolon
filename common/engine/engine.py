import esper

# Ugly
from .processor import ProcessorClass
from .resource import Resource
from .resource_manager import ResourceManager
from .world import World


class Engine:
    def __init__(self):
        self._running = False
        self.world: World = World(esper.current_world)
        self.resource_manager: ResourceManager = ResourceManager()

    def run(self) -> None:
        self._running = True
        while self._running:
            self.world.update(self.resource_manager)

    def register_resource(self, resource: Resource) -> None:
        self.resource_manager.add_resource(resource)

    def add_processor(self, processor: ProcessorClass) -> None:
        self.world.add_processor(processor)

    def stop(self):
        self._running = False
