from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def build(self, engine: "Engine") -> None:
        pass
