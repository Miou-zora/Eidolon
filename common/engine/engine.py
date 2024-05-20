from typing import Set
from typing import Type

import esper

from .plugin import Plugin

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
        self.plugins: Set[Type["Plugin"]] = set()

    def run(self) -> None:
        for plugin in self.plugins:
            plugin().build(self)
        self._running = True
        self.world.update(ScheduleLabel.Startup, self.resource_manager)
        while self._running:
            self.world.update(ScheduleLabel.Update, self.resource_manager)

    def __insert_resource(self, resource: Type[Resource]) -> "Engine":
        self.resource_manager.insert_resource(resource(engine=self))
        return self

    def insert_resources(self, *resources: Type[Resource]) -> "Engine":
        for resource in resources:
            self.__insert_resource(resource)
        return self

    def __add_processor(
        self, schedule: ScheduleLabel, processor: ProcessorClass
    ) -> "Engine":
        self.world.add_processor(schedule, processor)
        return self

    def add_processors(
        self, schedule: ScheduleLabel, *processors: ProcessorClass
    ) -> "Engine":
        for processor in processors:
            self.__add_processor(schedule, processor)
        return self

    def stop(self):
        self._running = False

    def __add_plugin(self, plugin: Type[Plugin]) -> "Engine":
        self.plugins.add(plugin)

    def add_plugins(self, *plugins):
        for plugin in plugins:
            self.__add_plugin(plugin)
        return self
