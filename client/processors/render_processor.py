import pyray

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager


class RenderProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        pyray.begin_drawing()
        pyray.clear_background(pyray.RAYWHITE)
        pyray.draw_text(
            "Congrats! You created your first window!", 190, 200, 20, pyray.LIGHTGRAY
        )
        pyray.end_drawing()
