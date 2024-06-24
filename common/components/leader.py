from common.engine import component
from common.utils.debug import Debug


@component
class Leader(Debug):
    ent: int
    attraction: float
