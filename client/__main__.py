from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import esper
import raylib

from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.plugin import Plugin
from common.engine.processor import Processor
from common.engine.schedule_label import ScheduleLabel
from common.utils.vector2 import Vector2
from components.box_collider import BoxCollider
from components.clickable import Clickable
from components.drawable import Drawable
from plugins.default_plugin import DefaultPlugin
from plugins.scene_plugin import ScenePlugin
from processors.click_processor import ClickProcessor
from resources.assets_manager import AssetsManager
from resources.scene_manager import Scene, SceneManager
from resources.window_resource import WindowResource

if TYPE_CHECKING:
    from common.engine.resource_manager import ResourceManager

from resources.network_manager import NetworkManager

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


class Setup(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        asset_manager = r.get_resource(AssetsManager)

        asset_manager.load_texture("StartButton", "assets/StartButton.png")
        asset_manager.load_texture("ExitButton", "assets/ExitButton.png")

        window = r.get_resource(WindowResource)
        window.background_color = raylib.DARKGRAY


class GameScene(Scene):
    def __init__(self):
        super().__init__()

    def on_start(self, r: ResourceManager) -> None:
        pass

    def on_exit(self, r: ResourceManager) -> None:
        pass


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.buttons: list[Entity] = []

    def on_start(self, r: ResourceManager) -> None:
        assets_manager = r.get_resource(AssetsManager)
        window = r.get_resource(WindowResource)
        window_size: Vector2 = window.get_size()
        start_button_name = "StartButton"
        start_button_size = assets_manager.get_texture_size(start_button_name)
        start_button_pos = Vector2(
            window_size.x / 2 - start_button_size.x / 2,
            window_size.y / 2 - start_button_size.y / 2,
        )
        self.buttons.append(
            Entity().add_components(
                Position(start_button_pos.x, start_button_pos.y),
                Name("Play Button"),
                Drawable(start_button_name),
                Clickable(lambda: r.get_resource(SceneManager).switch_to(GameScene())),
                BoxCollider(start_button_size),
            )
        )
        exit_button_name = "ExitButton"
        exit_button_size = assets_manager.get_texture_size(exit_button_name)
        exit_button_pos = Vector2(
            window_size.x / 2 - exit_button_size.x / 2,
            window_size.y / 2 - exit_button_size.y / 2 + 100,
        )
        self.buttons.append(
            Entity().add_components(
                Position(exit_button_pos.x, exit_button_pos.y),
                Name("Exit Button"),
                Drawable(exit_button_name),
                Clickable(lambda: r.get_resource(SceneManager).exit()),
                BoxCollider(exit_button_size),
            )
        )

    def on_exit(self, r: ResourceManager) -> None:
        for ent in self.buttons:
            esper.delete_entity(ent.id)


class StartProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        scene_manager = r.get_resource(SceneManager)
        scene_manager.switch_to(MainMenu())


class ClientPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.add_processors(
            ScheduleLabel.Startup,
            Setup(),
            StartProcessor(),
        ).add_processors(
            ScheduleLabel.Update,
            ClickProcessor(),
        ).insert_resources(
            NetworkManager
        )


def run():
    engine: Engine = Engine()
    # add common resources
    engine.add_plugins(
        DefaultPlugin().build(),
    )

    engine.add_plugins(
        ScenePlugin,
        ClientPlugin,
    )

    engine.run()


if __name__ == "__main__":
    run()
