from common.engine import component

from common.utils.debug import Debug

@component
class Drawable(Debug):
    texture_name: str
    # TODO: find a way to extract this from Text and Drawable components
    # 0 is the farthest away
    z_order: int = 0
    # -1 is no camera
    camera_id: int = -1

