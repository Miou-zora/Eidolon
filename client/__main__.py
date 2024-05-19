import logging

from common.components.name import Name
from common.components.position import Position
from common.engine.engine import Engine
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.engine.schedule_label import ScheduleLabel
from common.processors.log_processor import LogProcessor
from common.processors.real_time_provider_processor import \
    RealTimeProviderProcessor
from common.resources.time_providers.real_time_provider import RealTimeProvider
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

        asset_name = "randomImage"
        asset_manager.load_texture(asset_name, f"assets/randomImage.png")

        _: Entity = Entity().add_components(
            Position(300, 300),
            Name("First Entity"),
            Drawable(asset_name),
            Controllable(),
            Speed(300),
        )


def run():
    engine: Engine = Engine()

    engine.insert_resources(
        WindowResource,
        AssetsManager,
        InputsManager,
        RealTimeProvider,
    ).add_processors(
        ScheduleLabel.Startup,
        Setup(),
    ).add_processors(
        ScheduleLabel.Update,
        RealTimeProviderProcessor(),
        WindowProcessor(engine),
        RenderProcessor(),
        InputsUpdateProcessor(),
        ControlProcessor(),
        LogProcessor(),
    )

    engine.run()


if __name__ == "__main__":
    run()
