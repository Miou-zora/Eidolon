from common.engine import component


@component
class Temporary:
    duration: float
    elapsed: float = 0
