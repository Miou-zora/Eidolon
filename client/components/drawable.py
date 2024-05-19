from common.engine import component


@component
class Drawable:
    texture_name: str

    def __str__(self) -> str:
        return f"DrawableComponent(textureName:{self.texture_name})"
