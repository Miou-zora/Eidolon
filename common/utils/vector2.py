import pyray as raylib


class Vector2:
    def __init__(self, x: float, y: float):
        self.__vec: raylib.Vector2 = raylib.Vector2(x, y)

    @property
    def x(self) -> float:
        return self.__vec.x

    @property
    def y(self) -> float:
        return self.__vec.y

    @x.setter
    def x(self, value: float):
        self.__vec.x = value

    @y.setter
    def y(self, value: float):
        self.__vec.y = value
