from common.engine import component
from common.engine.entity import Entity


@component
class Leader:
    ent: Entity
    attraction: float

    def __str__(self) -> str:
        return f"Follow(Leader={self.ent.id})"
