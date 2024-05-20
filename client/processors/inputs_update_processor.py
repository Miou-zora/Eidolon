from resources.inputs_manager import InputsManager

from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager


class InputsUpdateProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        inputs_manager = r.get_resource(InputsManager)
        inputs_manager.update()
