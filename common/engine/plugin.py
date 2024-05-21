from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common.engine.engine import Engine


class Plugin(ABC):
    @abstractmethod
    def build(self, engine: Engine) -> None:
        pass

    def ready(self, _: Engine) -> bool:
        return True

    def finish(self, engine: Engine) -> None:
        pass

    def cleanup(self, engine: Engine) -> None:
        pass

    @classmethod
    def name(cls) -> str:
        return cls.__name__

    def is_unique(self) -> bool:
        return True

    def add_to_app(self, engine: Engine) -> None:
        self.build(engine)
