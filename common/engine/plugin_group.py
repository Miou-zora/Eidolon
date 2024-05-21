from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from common.engine.plugin import Plugin

if TYPE_CHECKING:
    from common.engine.engine import Engine
    from common.engine.plugin_group_builder import PluginGroupBuilder


class PluginGroup(ABC):
    @abstractmethod
    def build(self) -> PluginGroupBuilder:
        pass

    def set(self, plugin: Plugin) -> PluginGroupBuilder:
        return self.build().set(plugin)

    def add_to_app(self, engine: Engine) -> None:
        self.build().finish(engine)
