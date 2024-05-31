import pymunk

from common.engine import component


@component
class Physic:
    body: pymunk.Body
    shape: pymunk.Shape

    def __str__(self) -> str:
        return f"PhysicBody({repr(self.body)}, {repr(self.shape)})"
