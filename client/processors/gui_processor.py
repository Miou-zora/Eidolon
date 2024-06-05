import logging

import esper
import pyray as raylib

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.gui_button import GUIButton

DEBUG_COLLIDER = True

logger = logging.getLogger(__name__)


class GUIProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        for ent, button in esper.get_component(GUIButton):
            if raylib.gui_button(button.size, button.text):
                button.state = True
