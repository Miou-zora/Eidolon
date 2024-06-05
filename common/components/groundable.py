from common.engine import component


@component
class Groundable:
    grounded: bool = False
