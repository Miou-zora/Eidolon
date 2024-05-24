from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel
from processors.switch_scene_processor import SwitchSceneProcessor
from resources.scene_manager import SceneManager


class ScenePlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(SceneManager).add_processors(
            ScheduleLabel.Update, SwitchSceneProcessor()
        )
