import pyray

from common.engine.engine import Engine
from common.engine.resource import Resource


class WindowResource(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        pyray.init_window(1600, 900, "Eidolon Engine")
