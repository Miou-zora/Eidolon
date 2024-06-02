from __future__ import annotations

import logging
from typing import TYPE_CHECKING

import esper
import raylib

from common.components.leader import Leader
from common.components.name import Name
from common.components.position import Position
from common.components.temporary import Temporary
from common.components.velocity import Velocity
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.plugin import Plugin
from common.engine.processor import Processor
from common.engine.schedule_label import ScheduleLabel
from common.processors.follow_leader_processor import FollowLeaderProcessor
from common.processors.temporary_processor import TemporaryProcessor
from common.utils.vector2 import Vector2
from components.box_collider import BoxCollider
from components.camera import Camera2D
from components.controllable import Controllable
from components.drawable import Drawable
from components.gui_button import GUIButton
from components.speed import Speed
from components.text import Text
from plugins.default_plugin import DefaultPlugin
from plugins.scene_plugin import ScenePlugin
from processors.click_processor import ClickProcessor
from processors.control_processor import ControlProcessor
from processors.gui_button_processor import GUIButtonProcessor
from resources.assets_manager import AssetsManager
from resources.scene_manager import Scene, SceneManager
from resources.window_resource import WindowResource

if TYPE_CHECKING:
    from common.engine.resource_manager import ResourceManager
    from typing import Callable

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
        asset_manager.load_texture("Player", "assets/Player.png")

        window = r.get_resource(WindowResource)
        window.background_color = raylib.DARKGRAY

        camera = Entity().add_components(
            Camera2D(Vector2(0, 0), 0, 1),
            Position(0, 0),
            Leader(-1, 5),
            Velocity(),
        )


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        # Maybe inherit from Scene class
        self.entities: list[Entity] = []

    def on_start(self, r: ResourceManager) -> None:
        asset_manager = r.get_resource(AssetsManager)
        player_texture_name = "Player"
        player_spawn_pos = Vector2(300, 300)
        self.entities = [
            Entity().add_components(
                Position(player_spawn_pos.x, player_spawn_pos.y),
                Name("First Entity"),
                Drawable(player_texture_name),
                BoxCollider(asset_manager.get_texture_size(player_texture_name)),
                Controllable(),
                Speed(300),
                Velocity(),
            ),
            Entity().add_components(
                Text(value="Hello World"),
                Temporary(5),
                Position(100, 100),
            ),
        ]
        window = r.get_resource(WindowResource)
        for ent, (pos, cam, lead) in esper.get_components(Position, Camera2D, Leader):
            lead.ent = self.entities[0].id
            cam.offset.x = window.get_size().x / 2
            cam.offset.y = window.get_size().y / 2

    def on_exit(self, r: ResourceManager) -> None:
        for ent in self.entities:
            esper.delete_entity(ent.id)


class MainMenu(Scene):
    def __init__(self):
        super().__init__()
        self.buttons: list[Entity] = []

    def on_start(self, r: ResourceManager) -> None:
        assets_manager = r.get_resource(AssetsManager)
        window = r.get_resource(WindowResource)
        scene_manager = r.get_resource(SceneManager)
        window_size: Vector2 = window.get_size()

        self.buttons = [
            MainMenu.__create_start_button(assets_manager, window_size, scene_manager),
            MainMenu.__create_exit_button(assets_manager, window_size, scene_manager),
        ]

    @staticmethod
    def __create_start_button(
        assets_manager: AssetsManager,
        window_size: Vector2,
        scene_manager: SceneManager,
    ) -> Entity:
        start_button_name = "StartButton"
        start_button_size = assets_manager.get_texture_size(start_button_name)
        start_button_pos = Vector2(
            window_size.x / 2 - start_button_size.x / 2,
            window_size.y / 2 - start_button_size.y / 2 - 100,
        )
        return MainMenu.__create_button(
            start_button_name,
            start_button_pos,
            start_button_size,
            "Start",
            lambda: scene_manager.switch_to(GameScene()),
        )

    @staticmethod
    def __create_exit_button(
        assets_manager: AssetsManager,
        window_size: Vector2,
        scene_manager: SceneManager,
    ) -> Entity:
        exit_button_name = "ExitButton"
        exit_button_size = assets_manager.get_texture_size(exit_button_name)
        exit_button_pos = Vector2(
            window_size.x / 2 - exit_button_size.x / 2,
            window_size.y / 2 - exit_button_size.y / 2,
        )
        return MainMenu.__create_button(
            exit_button_name,
            exit_button_pos,
            exit_button_size,
            "Exit",
            lambda: scene_manager.exit(),
        )

    @staticmethod
    def __create_button(
        name: str, pos: Vector2, size: Vector2, text: str, callback: Callable[[], None]
    ) -> Entity:
        # We will maybe create a proper Button creator in the future (and use raygui)
        return Entity().add_components(
            GUIButton(pos, size, text, callback),
            Name(name),
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
            ControlProcessor(),
            FollowLeaderProcessor(),
            GUIButtonProcessor(),
            TemporaryProcessor(),
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
