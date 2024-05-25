from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine import component

if TYPE_CHECKING:
    from typing import Callable


@component
class Clickable:
    # maybe have an async callback function here
    __call: Callable[[], None] = lambda: None

    def __str__(self) -> str:
        if self.__call.__name__ == "<lambda>":
            return f"ClickableComponent(call:lambda({id(self.__call):x}))"
        return f"ClickableComponent(call:{self.__call.__name__})"

    def __call__(self):
        self.__call()
