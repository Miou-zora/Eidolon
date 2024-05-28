import pymunk

from common.engine import component


@component
class PhysicBody:
    body: pymunk.Body
    shape: pymunk.Shape

    def __str__(self) -> str:
        return f"PhysicBody()"
