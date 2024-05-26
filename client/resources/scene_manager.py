from __future__ import annotations

import logging  # TODO: use proper logging lib
from abc import ABC
from abc import abstractmethod
from typing import TYPE_CHECKING
from typing import final

from common.engine.engine import Engine
from common.engine.resource import Resource

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)


class Scene(ABC):
    @abstractmethod
    def on_start(self) -> None:
        # maybe add some parameters like engine to kill entity (for example)
        pass

    @abstractmethod
    def on_exit(self) -> None:
        pass


@final
class DefaultScene(Scene):
    def on_start(self) -> None:
        pass

    def on_exit(self) -> None:
        pass


class SceneManager(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.scene_history: list[Scene] = [DefaultScene()]
        self.next_scene: Scene | None = None
        self.rollback_scene: bool = False
        self.index: int = 0

    def switch_to(self, scene: Scene) -> None:
        self.next_scene = scene

    def go_back_to_previous_scene(self) -> None:
        if self.index == 0:
            return
        if self.next_scene is not None:
            self.next_scene = None
        self.rollback_scene = True

    def __add_scene_to_history(self, scene: Scene) -> None:
        self.scene_history.append(scene)

    def __switch_to_next_scene(self) -> None:
        self.scene_history[self.index].on_exit()
        if self.index != len(self.scene_history) - 1:
            self.scene_history = self.scene_history[: self.index + 1]
        self.index += 1
        self.scene_history.append(self.next_scene)
        self.scene_history[self.index].on_start()

    def __switch_to_previous_scene(self) -> None:
        self.scene_history[self.index].on_exit()
        self.index -= 1
        self.scene_history[self.index].on_start()

    def update_scene(self) -> None:
        if self.rollback_scene:
            self.__switch_to_previous_scene()
        if self.next_scene is not None:
            self.__switch_to_next_scene()
        self.next_scene = None
        self.rollback_scene = False
