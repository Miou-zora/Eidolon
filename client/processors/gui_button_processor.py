import logging

import esper

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from components.gui_button import GUIButton

logger = logging.getLogger(__name__)


class GUIButtonProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        for ent, button in esper.get_component(GUIButton):
            if button.state:
                button()
                button.state = False
