from common.engine import component


@component
class BoxCollider:
    width: float
    height: float

    def __str__(self) -> str:
        return f"BoxCollider(width:{self.width}, height:{self.height})"
