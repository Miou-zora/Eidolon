from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel
from common.engine.time_providers import RealTimeProvider
from common.processors.real_time_provider_processor import RealTimeProviderProcessor


class TimePlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(RealTimeProvider).add_processors(
            ScheduleLabel.Update, RealTimeProviderProcessor()
        )
