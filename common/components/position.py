from __future__ import annotations

from common.engine import component
from common.utils.vector2 import Vector2


@component
class Position:
    __size: Vector2

    @classmethod
    def from_size(cls, x: float, y: float) -> Position:
        return cls(Vector2(x, y))

    def __init__(self, vector: Vector2) -> None:
        self.__size = vector

    @property
    def x(self) -> float:
        return self.__size.x

    @property
    def y(self) -> float:
        return self.__size.y

    @x.setter
    def x(self, x: float) -> None:
        self.__size.x = x

    @y.setter
    def y(self, y: float) -> None:
        self.__size.y = y

    def __str__(self) -> str:
        return f"Position({self.x},{self.y})"
