from common.engine import component


@component
class Drawable:
    texture_name: str
    # TODO: find a way to extract this from Text and Drawable components
    # 0 is the farthest away
    z_order: int = 0
    # -1 is no camera
    camera_id: int = -1

    def __str__(self) -> str:
        return f"DrawableComponent(textureName:{self.texture_name})"
