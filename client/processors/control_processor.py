import esper
import pyray as raylib
from components.controllable import Controllable
from components.speed import Speed
from resources.inputs_manager import InputsManager

from common.components.position import Position
from common.engine import Processor
from common.engine.resource_manager import ResourceManager
from common.resources.time_providers.time_provider import TimeProvider


class ControlProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        inputs_manager: InputsManager = r.get_resource(InputsManager)
        time_provider: TimeProvider = r.get_resource(TimeProvider)
        if inputs_manager is None:
            raise NotImplemented(f"Resource not found: InputsManager:{inputs_manager}")
        for ent, (_, pos, speed) in esper.get_components(Controllable, Position, Speed):
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_W):
                pos.y -= time_provider.get_elapsed_time() * speed.value
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_S):
                pos.y += time_provider.get_elapsed_time() * speed.value
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_A):
                pos.x -= time_provider.get_elapsed_time() * speed.value
            if inputs_manager.is_key_pressed(raylib.KeyboardKey.KEY_D):
                pos.x += time_provider.get_elapsed_time() * speed.value
