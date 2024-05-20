from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel
from common.processors.real_time_provider_processor import RealTimeProviderProcessor
from common.resources.time_providers.real_time_provider import RealTimeProvider


class TimePlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(RealTimeProvider).add_processors(
            ScheduleLabel.Update, RealTimeProviderProcessor()
        )
