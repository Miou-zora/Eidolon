from common.engine.engine import Engine
from common.engine.plugin import Plugin
from common.resources.time_providers.unit_time_provider import UnitTimeProvider


class TimePlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(UnitTimeProvider)
