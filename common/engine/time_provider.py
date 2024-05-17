from abc import ABC, abstractmethod

from .time import TimeUnit


class TimeProvider(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def get_elapsed_time(self) -> TimeUnit:
        return 1
