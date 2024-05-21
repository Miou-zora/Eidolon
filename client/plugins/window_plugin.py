from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel
from processors.render_processor import RenderProcessor
from processors.window_processor import WindowProcessor
from resources.window_resource import WindowResource

if TYPE_CHECKING:
    from common.engine.engine import Engine


class WindowPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(WindowResource).add_processors(
            ScheduleLabel.Update,
            WindowProcessor(engine),
            RenderProcessor(),
        )
