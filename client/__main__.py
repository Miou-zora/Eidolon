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
from components.controllable import Controllable
from components.drawable import Drawable
from components.speed import Speed
from plugins.default_plugin import DefaultPlugin
from processors.control_processor import ControlProcessor
from resources.assets_manager import AssetsManager

if TYPE_CHECKING:
    from common.engine.resource_manager import ResourceManager

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


class Setup(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        asset_manager: AssetsManager = r.get_resource(AssetsManager)

        asset_name = "randomImage"
        asset_manager.load_texture(asset_name, f"assets/randomImage.png")

        _: Entity = Entity().add_components(
            Position(300, 300),
            Name("First Entity"),
            Drawable(asset_name),
            Controllable(),
            Speed(300),
        )


class ClientPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.add_processors(
            ScheduleLabel.Startup,
            Setup(),
        ).add_processors(
            ScheduleLabel.Update,
            # LogProcessor(),
            ControlProcessor(),
        )


def run():
    engine: Engine = Engine()

    engine.add_plugins(
        DefaultPlugin().build(),
        ClientPlugin,
    )

    engine.run()


if __name__ == "__main__":
    run()
