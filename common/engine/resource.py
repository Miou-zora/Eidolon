from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common.engine.engine import Engine


class Resource:
    def __init__(self, engine: Engine):
        self._engine = engine
