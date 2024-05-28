from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from common.engine.engine import Engine
from common.engine.resource import Resource
import pymunk


class PhysicResource(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.world: pymunk.Space | None = None

    def init_world(self) -> None:
        self.world = pymunk.Space()

    def update(self, dt: float) -> None:
        self.world.step(dt)
