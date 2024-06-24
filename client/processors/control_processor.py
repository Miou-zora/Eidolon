import logging

import esper
import pyray as raylib

from common.components.velocity import Velocity
from common.engine import Processor
from common.engine.resource_manager import ResourceManager
from components.controllable import Controllable
from components.speed import Speed
from resources.inputs_manager import InputsManager

logger = logging.getLogger(__name__)


class ControlProcessor(Processor):

    def process(self, r: ResourceManager) -> None:
        inputs_manager = r.get_resource(InputsManager)
        for ent, (_, vel, speed) in esper.get_components(Controllable, Velocity, Speed):
            vel.x += (
                inputs_manager.is_key_down(raylib.KeyboardKey.KEY_D)
                - inputs_manager.is_key_down(raylib.KeyboardKey.KEY_A)
            ) * speed.value

            vel.y += (
                inputs_manager.is_key_down(raylib.KeyboardKey.KEY_S)
                - inputs_manager.is_key_down(raylib.KeyboardKey.KEY_W)
            ) * speed.value
