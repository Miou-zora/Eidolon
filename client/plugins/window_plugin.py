from processors.render_processor import RenderProcessor
from processors.window_processor import WindowProcessor
from resources.window_resource import WindowResource

from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel


class WindowPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(WindowResource).add_processors(
            ScheduleLabel.Update,
            WindowProcessor(engine),
            RenderProcessor(),
        )
