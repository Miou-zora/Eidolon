from typing import Type

import esper

# Ugly
from .processor import ProcessorClass
from .resource import Resource
from .resource_manager import ResourceManager
from .schedule_label import ScheduleLabel
from .world import World


class Engine:

    def __init__(self):
        self._running = False
        self.world: World = World(esper.current_world)
        self.resource_manager: ResourceManager = ResourceManager()

    def run(self) -> None:
        self._running = True
        self.world.update(ScheduleLabel.Startup, self.resource_manager)
        while self._running:
            self.world.update(ScheduleLabel.Update, self.resource_manager)

    def register_resource(self, resource: Type[Resource]) -> "Engine":
        self.resource_manager.add_resource(resource(engine=self))
        return self

    def add_processor(
        self, schedule: ScheduleLabel, processor: ProcessorClass
    ) -> "Engine":
        self.world.add_processor(schedule, processor)
        return self

    def stop(self):
        self._running = False
