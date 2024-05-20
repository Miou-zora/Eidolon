from resources.assets_manager import AssetsManager

from common.engine.engine import Engine
from common.engine.plugin import Plugin


class AssetsPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(AssetsManager)
