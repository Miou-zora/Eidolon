from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from resources.scene_manager import SceneManager


class SwitchSceneProcessor(Processor):
    def process(self, r: ResourceManager) -> None:
        scene_manager = r.get_resource(SceneManager)
        scene_manager.update_scene()
