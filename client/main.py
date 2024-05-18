import logging
import os
import sys

from client.components.controllable import Controllable
from client.components.drawable import Drawable
from client.components.speed import Speed
from client.processors.control_processor import ControlProcessor
from client.processors.inputs_update_processor import InputsUpdateProcessor
from client.processors.render_processor import RenderProcessor
from client.processors.window_processor import WindowProcessor
from client.resources.assets_manager import AssetsManager
from client.resources.inputs_manager import InputsManager
from client.resources.window_resource import WindowResource
from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.resources.time_providers.unit_time_provider import UnitTimeProvider

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
    asset_path = f"{base_path}/client/assets/randomImage.png"
    asset_path_bytes = asset_path.encode("utf-8")
    asset_manager.load_texture("randomImage", asset_path_bytes)

    engine.register_resource(asset_manager)
    engine.register_resource(InputsManager())
    engine.register_resource(UnitTimeProvider())
    engine.add_processor(WindowProcessor(engine))
    engine.add_processor(RenderProcessor())
    engine.add_processor(InputsUpdateProcessor())
    engine.add_processor(ControlProcessor())

    entity: Entity = Entity()
    entity.add_component(Position(300, 300))
    entity.add_component(Name("First Entity"))
    entity.add_component(Drawable("randomImage"))
    entity.add_component(Controllable())
    entity.add_component(Speed(1))

    engine.run()


if __name__ == "__main__":
    run()
