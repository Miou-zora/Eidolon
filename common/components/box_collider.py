from __future__ import annotations

from common.engine import component
from common.utils.vector2 import Vector2


@component
class BoxCollider:
    __size: Vector2

    @classmethod
    def from_size(cls, x: int, y: int) -> BoxCollider:
        return cls(Vector2(x, y))

    def __init__(self, vector: Vector2) -> None:
        self.__size = vector

    @property
    def x(self) -> float:
        return self.__size.x

    @property
    def y(self) -> float:
        return self.__size.y

    @x.getter
    def x(self) -> float:
        return self.__size.x

    @y.getter
    def y(self) -> float:
        return self.__size.y

    def __str__(self) -> str:
        return f"BoxCollider(width:{self.x:.6f}, height:{self.y:.6f})"
