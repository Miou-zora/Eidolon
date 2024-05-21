from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine.plugin import Plugin
from resources.assets_manager import AssetsManager

if TYPE_CHECKING:
    from common.engine.engine import Engine


class AssetsPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.insert_resources(AssetsManager)
