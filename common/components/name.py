from common.engine import component


@component
class Name:
    name: str

    def __str__(self) -> str:
        return f"{self.name}"
