from common.engine.plugin_group import PluginGroup
from common.engine.plugin_group_builder import PluginGroupBuilder
from .assets_plugin import AssetsPlugin
from .inputs_plugin import InputsPlugin
from .time_plugin import TimePlugin
from .window_plugin import WindowPlugin


class DefaultPlugin(PluginGroup):
    def build(self) -> PluginGroupBuilder:
        gb = (
            PluginGroupBuilder(self.__class__)
            .add(WindowPlugin())
            .add(AssetsPlugin())
            .add(TimePlugin())
            .add(InputsPlugin())
        )
        return gb
