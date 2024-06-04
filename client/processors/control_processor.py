import logging

import esper
import pyray as raylib

from common.components.velocity import Velocity
from common.engine import Processor
from common.engine.resource_manager import ResourceManager
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
        network_manager = r.get_resource(NetworkManager)
        for ent, (_, vel, speed) in esper.get_components(Controllable, Velocity, Speed):
            if inputs_manager.is_key_down(raylib.KeyboardKey.KEY_W):
                vel.y -= speed.value
            if inputs_manager.is_key_down(raylib.KeyboardKey.KEY_S):
                vel.y += speed.value
            if inputs_manager.is_key_down(raylib.KeyboardKey.KEY_A):
                vel.x -= speed.value
            if inputs_manager.is_key_down(raylib.KeyboardKey.KEY_D):
                vel.x += speed.value
            # TODO: Change that :3
            #                   ↑ @huntears (https://cdn.discordapp.com/attachments/1225045089055801395/1236661856261636177/image.png?ex=6654821a&is=6653309a&hm=cc8bf2a766f85b05695fa1a1e80d1c82b755b729a45a256bfac0c613cf363cd7&)
            # network_manager.send_movement(vel)
