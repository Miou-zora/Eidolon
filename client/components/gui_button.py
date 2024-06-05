from __future__ import annotations

from typing import TYPE_CHECKING

import pyray as raylib

from common.engine import component
from common.utils.vector2 import Vector2

if TYPE_CHECKING:
    from typing import Callable

import logging

logger = logging.getLogger(__name__)


@component
class GUIButton:
    text: str
    size: raylib.Rectangle
    state: int = 0
    callback: Callable[[], None] = lambda: logger.info("Button clicked")

    def __init__(
        self, pos: Vector2, size: Vector2, text: str, callback: Callable[[], None]
    ) -> None:
        self.size = raylib.Rectangle(pos.x, pos.y, size.x, size.y)
        self.callback = callback
        self.text = text

    def __str__(self) -> str:
        if self.callback.__name__ == "<lambda>":
            return f"GUIButton(call:lambda({id(self.callback):x}))"
        return f"GUIButton(call:{self.callback.__name__})"

    def __call__(self):
        self.callback()
