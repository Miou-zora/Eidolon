import time

from common.engine.engine import Engine
from common.engine.time import TimeUnit
from common.resources.time_providers.time_provider import TimeProvider


class RealTimeProvider(TimeProvider):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self._unit: TimeUnit = 0
        self._last_time = self.get_current_time()

    def update(self) -> None:
        current_time = self.get_current_time()
        self._unit = current_time - self._last_time
        self._last_time = current_time

    def get_elapsed_time(self) -> TimeUnit:
        return self._unit

    def get_current_time(self) -> TimeUnit:
        return time.time()
