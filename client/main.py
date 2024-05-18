import logging
import os
import sys

from client.components.drawable import Drawable
from client.processors.render_processor import RenderProcessor
from client.processors.window_processor import WindowProcessor
from client.resources.assets_manager import AssetsManager
from client.resources.window_resource import WindowResource
from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


def run():
    engine: Engine = Engine()
    engine.register_resource(WindowResource())

    asset_manager: AssetsManager = AssetsManager()
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    asset_manager.load_texture(
        "randomImage", f"{base_path}/client/assets/randomImage.png"
    )

    engine.register_resource(asset_manager)
    engine.add_processor(WindowProcessor(engine))
    engine.add_processor(RenderProcessor())

    entity: Entity = Entity()
    entity.add_component(Position(300, 300))
    entity.add_component(Name("First Entity"))
    entity.add_component(Drawable("randomImage"))

    engine.run()


if __name__ == "__main__":
    run()
