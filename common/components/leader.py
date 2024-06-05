from common.engine import component


@component
class Leader:
    ent: int
    attraction: float

    def __str__(self) -> str:
        return f"Follow(Leader={self.ent})"
