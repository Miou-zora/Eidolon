from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.plugin import Plugin
from common.engine.processor import Processor
from common.engine.schedule_label import ScheduleLabel
from common.resources.time_providers.real_time_provider import RealTimeProvider
from components.box_collider import BoxCollider
from components.clickable import Clickable
from components.controllable import Controllable
from components.drawable import Drawable
from components.speed import Speed
from plugins.default_plugin import DefaultPlugin
from plugins.scene_plugin import ScenePlugin
from processors.click_processor import ClickProcessor
from processors.connection_processor import ConnectionProcessor
from processors.control_processor import ControlProcessor
from resources.assets_manager import AssetsManager
from resources.scene_manager import SceneManager, Scene

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
        network_manager = r.get_resource(NetworkManager)

        asset_name = "randomImage"
        asset_manager.load_texture(asset_name, "assets/randomImage.png")
        asset_size = asset_manager.get_texture_size(asset_name)

        network_manager.launch()

        def TestClickableFunction():
            TestClickableFunction.i += 1
            logger.debug("Clicked %i", TestClickableFunction.i)

        TestClickableFunction.i = 0
        _: Entity = Entity().add_components(
            Position(300, 300),
            Name("First Entity"),
            Drawable(asset_name),
            Clickable(TestClickableFunction),
            BoxCollider(asset_size),
            Controllable(),
            Speed(300),
        )


class TestScene(Scene):
    def on_start(self) -> None:
        logger.info("TestScene started")

    def on_exit(self) -> None:
        logger.info("TestScene exited")


class TestSceneProcessor(Processor):
    def __init__(self):
        super().__init__()
        self.chrono = 0
        self.time_to_change_scene = 5  # seconds

    def process(self, r: ResourceManager) -> None:
        scene_manager = r.get_resource(SceneManager)
        time_provider = r.get_resource(RealTimeProvider)
        self.chrono += time_provider.get_elapsed_time()
        if self.chrono >= self.time_to_change_scene:
            scene_manager.switch_to(TestScene())
            self.chrono -= self.time_to_change_scene


class ClientPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.add_processors(
            ScheduleLabel.Startup,
            Setup(),
        ).add_processors(
            ScheduleLabel.Update,
            # LogProcessor(),
            ControlProcessor(),
            ConnectionProcessor(),
            ClickProcessor(),
            TestSceneProcessor(),
        ).insert_resources(NetworkManager)


def run():
    engine: Engine = Engine()

    engine.add_plugins(
        DefaultPlugin().build(),
        ClientPlugin,
        ScenePlugin(),
    )

    engine.run()


if __name__ == "__main__":
    run()
