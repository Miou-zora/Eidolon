from dataclasses import asdict, dataclass, field
from common.components.position import Position
from typing import Any
from enum import Enum
import json


@dataclass
class MoveToPosition:
    new_pos: Position = field(default_factory=Position)


@dataclass
class Connection:
    name: str


@dataclass
class Disconnection:
    ...


@dataclass
class Packet:
    t: str
    # TODO: Type this omegalul
    data: Any

    def ser(self) -> bytes:
        return str.encode(json.dumps(asdict(self)))
