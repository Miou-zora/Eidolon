from common.engine import component


@component
class Position:
    x: float = 0.0
    y: float = 0.0

    def __str__(self) -> str:
        return f"Position({self.x},{self.y})"
