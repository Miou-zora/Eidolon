from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common.engine.engine import Engine
    from common.engine.time import TimeUnit
from common.engine.time_providers.time_provider import TimeProvider


class UnitTimeProvider(TimeProvider):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self._unit: TimeUnit = 1

    def update(self) -> None:
        pass

    def get_elapsed_time(self) -> TimeUnit:
        return self._unit
