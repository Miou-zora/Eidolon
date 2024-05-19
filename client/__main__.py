import logging

from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.engine.schedule_label import ScheduleLabel
from common.processors.log_processor import LogProcessor
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


class Setup(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        asset_manager: AssetsManager = r.get_resource(AssetsManager)
        asset_manager.load_texture("randomImage", f"assets/randomImage.png")


def run():
    engine: Engine = (
        Engine()
        .register_resource(WindowResource)
        .register_resource(AssetsManager)
        .register_resource(InputsManager)
        .register_resource(UnitTimeProvider)
    )
    engine.add_processor(ScheduleLabel.Startup, Setup())
    engine.add_processor(ScheduleLabel.Update, WindowProcessor(engine))
    engine.add_processor(ScheduleLabel.Update, RenderProcessor())
    engine.add_processor(ScheduleLabel.Update, InputsUpdateProcessor())
    engine.add_processor(ScheduleLabel.Update, ControlProcessor())
    engine.add_processor(ScheduleLabel.Update, LogProcessor())

    _: Entity = (
        Entity()
        .add_component(Position(300, 300))
        .add_component(Name("First Entity"))
        .add_component(Drawable("randomImage"))
        .add_component(Controllable())
        .add_component(Speed(1))
    )

    engine.run()


if __name__ == "__main__":
    run()
