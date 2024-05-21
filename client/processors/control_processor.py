import esper
import pyray as raylib
from components.controllable import Controllable
from components.speed import Speed
from resources.inputs_manager import InputsManager
from resources.network_manager import NetworkManager

from common.components.position import Position
from common.engine import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers.real_time_provider import RealTimeProvider


class ControlProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        inputs_manager = r.get_resource(InputsManager)
        time_provider = r.get_resource(RealTimeProvider)
        network_manager = r.get_resource(NetworkManager)
        for ent, (_, pos, speed) in esper.get_components(Controllable, Position, Speed):
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_W):
                pos.y -= time_provider.get_elapsed_time() * speed.value
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_S):
                pos.y += time_provider.get_elapsed_time() * speed.value
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_A):
                pos.x -= time_provider.get_elapsed_time() * speed.value
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_D):
                pos.x += time_provider.get_elapsed_time() * speed.value
            # TODO: Change that :3
            network_manager.send_movement(pos)
