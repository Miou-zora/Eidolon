from common.engine import component


@component
class StaticBody:
    def __str__(self) -> str:
        return "StaticBody()"
