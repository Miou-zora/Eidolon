from enum import Enum, auto


class ScheduleLabel(Enum):
    Startup = auto()
    Update = auto()
    FixedUpdate = auto()
