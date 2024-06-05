from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from common.engine.resource import Resource

if TYPE_CHECKING:
    from common.engine.time import TimeUnit


class TimeProvider(ABC, Resource):
    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def get_elapsed_time(self) -> TimeUnit:
        return 1
