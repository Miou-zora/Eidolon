import raylib

from common.engine.resource import Resource


class WindowResource(Resource):
    def __init__(
        self, width: int = 1600, height: int = 900, title: bytes = b"Eidolon Engine"
    ):
        raylib.InitWindow(width, height, title)
