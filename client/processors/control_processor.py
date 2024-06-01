import logging

import esper
import pyray as raylib

from common.components.physic_body import Physic
from common.engine import Processor
from common.engine.resource_manager import ResourceManager
from common.engine.time_providers import RealTimeProvider
from components.controllable import Controllable
from components.speed import Speed
from resources.inputs_manager import InputsManager
from resources.network_manager import NetworkManager

logger = logging.getLogger(__name__)


class ControlProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        inputs_manager = r.get_resource(InputsManager)
        time_provider = r.get_resource(RealTimeProvider)
        network_manager = r.get_resource(NetworkManager)
        for ent, (_, physic, speed) in esper.get_components(
            Controllable, Physic, Speed
        ):
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_A):
                physic.body.velocity += (-speed.value * 0.05, 0)
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_D):
                physic.body.velocity += (speed.value * 0.05, 0)
            # TODO: Change that :3
            #                   ↑ @huntears (https://cdn.discordapp.com/attachments/1225045089055801395/1236661856261636177/image.png?ex=6654821a&is=6653309a&hm=cc8bf2a766f85b05695fa1a1e80d1c82b755b729a45a256bfac0c613cf363cd7&)
            # network_manager.send_movement(pos)
