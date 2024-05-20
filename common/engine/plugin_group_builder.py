import logging
from inspect import signature
from typing import TypeVar, Optional, Type

from common.engine.plugin import Plugin as Pl
from common.engine.plugin_group import PluginGroup

logger = logging.getLogger(__name__)

TypeId = signature(id).return_annotation
PluginType = TypeVar("PluginType", bound=Pl)


class PluginEntry:
    def __init__(self, plugin: Optional[Pl], enabled: bool):
        self.plugin: Optional[Pl] = plugin
        self.enabled: bool = enabled


class PluginGroupBuilder(PluginGroup):

    def __init__(self, plugin_group: Type[PluginGroup]):
        self.group_name: str = plugin_group.__name__
        self.plugins: dict[TypeId, PluginEntry] = {}
        self.order: list[TypeId] = []

    def build(self) -> "PluginGroupBuilder":
        return self

    def add(self, plugin: Pl) -> "PluginGroupBuilder":
        target_index = len(self.order)
        self.order.append(id(plugin.__class__))
        self.upsert_plugin_state(plugin, target_index)
        return self

    def upsert_plugin_state(self, plugin: Pl, added_at_index: int) -> None:
        self.upsert_plugin_entry_state(
            id(plugin.__class__),
            PluginEntry(plugin, True),
            added_at_index,
        )

    def upsert_plugin_entry_state(
        self, key: TypeId, plugin: PluginEntry, added_at_index: int
    ) -> None:
        if key in self.plugins:
            entry = self.plugins[key]
            if entry.enabled:
                logger.warning(
                    f"You are replacing plugin '{entry.plugin.name()}' that was not disabled."
                )
            if (
                to_remove := next(
                    (
                        i
                        for i, ty in enumerate(self.order)
                        if i != added_at_index and ty == key
                    ),
                    None,
                )
            ) is not None:
                self.order.pop(to_remove)
        self.plugins[key] = plugin

    def index_of(self, target: PluginType) -> int:
        try:
            return self.order.index(id(target))
        except ValueError:
            raise ValueError(f"Plugin does not exist in group: {target.__name__}.")

    def finish(self, engine: "Engine") -> None:
        for plugin_id in self.order:
            plugin = self.plugins[plugin_id]
            if plugin.enabled:
                plugin.plugin.add_to_app(engine)

    def disable(self, target: Type[PluginType]) -> "PluginGroupBuilder":
        plugin_entry = self.plugins.get(id(target))
        if plugin_entry is None:
            raise ValueError(
                f"Cannot disable a plugin that does not exist: {target.__name__}."
            )
        plugin_entry.enabled = False
        return self

    def enable(self, target: Type[PluginType]) -> "PluginGroupBuilder":
        plugin_entry = self.plugins.get(id(target))
        if plugin_entry is None:
            raise ValueError(
                f"Cannot enable a plugin that does not exist: {target.__name__}."
            )
        plugin_entry.enabled = True
        return self
