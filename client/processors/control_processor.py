import logging

import esper
import pyray as raylib

from common.components.physic_body import PhysicBody
from common.engine import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers.real_time_provider import RealTimeProvider
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
        for ent, (_, body, speed) in esper.get_components(
            Controllable, PhysicBody, Speed
        ):
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_A):
                body.body.velocity = (-1 * speed.value, 0 * speed.value)
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_D):
                body.body.velocity = (1 * speed.value, 0 * speed.value)
            # TODO: Change that :3
            #                   ↑ @huntears (https://cdn.discordapp.com/attachments/1225045089055801395/1236661856261636177/image.png?ex=6654821a&is=6653309a&hm=cc8bf2a766f85b05695fa1a1e80d1c82b755b729a45a256bfac0c613cf363cd7&)
            # network_manager.send_movement(pos)
