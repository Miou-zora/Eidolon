from processors.control_processor import ControlProcessor
from processors.inputs_update_processor import InputsUpdateProcessor
from processors.render_processor import RenderProcessor
from processors.window_processor import WindowProcessor
from resources.assets_manager import AssetsManager
from resources.inputs_manager import InputsManager
from resources.window_resource import WindowResource

from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel
from common.resources.time_providers.unit_time_provider import UnitTimeProvider


class DefaultPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(
            WindowResource,
            AssetsManager,
            InputsManager,
            UnitTimeProvider,
        ).add_processors(
            ScheduleLabel.Update,
            WindowProcessor(engine),
            RenderProcessor(),
            InputsUpdateProcessor(),
            ControlProcessor(),
        )
