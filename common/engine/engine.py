from __future__ import annotations

import logging
from typing import Type, TYPE_CHECKING

import esper

from .plugin import Plugin
from .plugin_group_builder import PluginGroupBuilder
from .resource_manager import ResourceManager
from .schedule_label import ScheduleLabel
from .world import World

if TYPE_CHECKING:
    from .processor import ProcessorClass
    from .resource import Resource

logger = logging.getLogger(__name__)


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

    def __insert_resource(self, resource: Type[Resource]) -> Engine:
        self.resource_manager.insert_resource(resource(engine=self))
        return self

    def insert_resources(self, *resources: Type[Resource]) -> Engine:
        for resource in resources:
            self.__insert_resource(resource)
        return self

    def __add_processor(
        self, schedule: ScheduleLabel, processor: ProcessorClass
    ) -> Engine:
        self.world.add_processor(schedule, processor)
        return self

    def add_processors(
        self, schedule: ScheduleLabel, *processors: ProcessorClass
    ) -> Engine:
        for processor in processors:
            self.__add_processor(schedule, processor)
        return self

    def stop(self):
        self._running = False

    def add_plugins(
        self,
        *plugins: Plugin | PluginGroupBuilder | Type[Plugin] | Type[PluginGroupBuilder],
    ) -> Engine:
        for plugin in plugins:
            if isinstance(plugin, Plugin) or isinstance(plugin, PluginGroupBuilder):
                plugin.add_to_app(self)
            else:
                plugin().add_to_app(self)
        return self
