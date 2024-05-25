from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine import component

if TYPE_CHECKING:
    from typing import Callable


@component
class Clickable:
    # maybe have an async callback function here
    call: Callable[[], None] = lambda: None

    def __str__(self) -> str:
        if self.call.__name__ == "<lambda>":
            return f"ClickableComponent(call:lambda({id(self.call):x}))"
        return f"ClickableComponent(call:{self.call.__name__})"
