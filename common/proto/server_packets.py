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
class ConfirmConnection:
    id: int


@dataclass
class Packet:
    t: str
    # TODO: Type this omegalul
    data: Any

    def ser(self) -> bytes:
        data = str.encode(json.dumps(asdict(self)))
        length = len(data)
        return length.to_bytes(length=4, signed=False) + data
