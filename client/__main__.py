import logging
import os
import sys

from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.resources.time_providers.unit_time_provider import UnitTimeProvider
from components.controllable import Controllable
from components.drawable import Drawable
from components.speed import Speed
from processors.control_processor import ControlProcessor
from processors.inputs_update_processor import InputsUpdateProcessor
from processors.render_processor import RenderProcessor
from processors.window_processor import WindowProcessor
from resources.assets_manager import AssetsManager
from resources.inputs_manager import InputsManager
from resources.window_resource import WindowResource

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


def run():
    engine: Engine = Engine()
    engine.register_resource(WindowResource())

    asset_manager: AssetsManager = AssetsManager()
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS + "/client"
    except Exception:
        base_path = os.path.abspath(".")  # This allows to run __main__ directly
        if not base_path.endswith("client"):
            base_path = os.path.abspath("./client")
    asset_manager.load_texture("randomImage", f"{base_path}/assets/randomImage.png")

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
