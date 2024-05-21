import json
from dataclasses import asdict, dataclass, field
from typing import Any

from common.components.position import Position


class PacketData:
    ...


@dataclass
class MoveToPosition(PacketData):
    new_pos: Position = field(default_factory=Position)


@dataclass
class Connection(PacketData):
    name: str


@dataclass
class Disconnection(PacketData): ...


@dataclass
class ConfirmConnection(PacketData):
    id: int


@dataclass
class OMoveToPosition(PacketData):
    new_pos: Position
    id: int


@dataclass
class Packet:
    t: str
    # TODO: Type this omegalul
    data: PacketData

    def ser(self) -> bytes:
        data = str.encode(json.dumps(asdict(self)))
        length = len(data)
        return length.to_bytes(length=4, signed=False, byteorder="big") + data
