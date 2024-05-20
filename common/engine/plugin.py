from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def build(self, engine: "Engine") -> None:
        pass

    def ready(self, engine: "Engine") -> bool:
        return True

    def finish(self, engine: "Engine") -> None:
        pass

    def cleanup(self, engine: "Engine") -> None:
        pass

    def name(self) -> str:
        return self.__class__.__name__

    def is_unique(self) -> bool:
        return True

    def add_to_app(self, engine: "Engine") -> None:
        self.build(engine)
