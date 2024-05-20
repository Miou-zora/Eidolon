from abc import ABC, abstractmethod

from common.engine.plugin import Plugin


class PluginGroup(ABC):
    @abstractmethod
    def build(self) -> "PluginGroupBuilder":
        pass

    def set(self, plugin: Plugin) -> "PluginGroupBuilder":
        return self.build().set(plugin)

    def add_to_app(self, engine: "Engine") -> None:
        self.build().finish(engine)
