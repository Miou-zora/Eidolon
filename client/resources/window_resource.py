import pyray

from common.engine.resource import Resource


class WindowResource(Resource):
    def __init__(
        self, width: int = 1600, height: int = 900, title: str = "Eidolon Engine"
    ):
        pyray.init_window(width, height, title)
