from processors.inputs_update_processor import InputsUpdateProcessor
from resources.inputs_manager import InputsManager

from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel


class InputsPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(InputsManager).add_processors(
            ScheduleLabel.Update,
            InputsUpdateProcessor(),
        )
