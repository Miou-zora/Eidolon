from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine.resource import Resource

if TYPE_CHECKING:
    from common.engine.engine import Engine


class PhysicResource(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.gravity = 1
