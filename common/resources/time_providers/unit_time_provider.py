from common.engine.time import TimeUnit
from common.resources.time_providers.time_provider import TimeProvider


class UnitTimeProvider(TimeProvider):
    def __init__(self, unit: TimeUnit = 1):
        self._unit: TimeUnit = unit

    def update(self) -> None:
        pass

    def get_elapsed_time(self) -> TimeUnit:
        return self._unit
