import json
import logging
import socket
import socketserver
import threading
import time
from dataclasses import dataclass, field

import common.proto.server_packets as srv_pck
from common.components.position import Position

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)


@dataclass
class ClientData:
    pos: Position = field(default_factory=Position)
    name: str = field(default_factory=str)
    inbound_buffer: bytes = field(default_factory=bytes)
    sock: socket.socket = field(default_factory=socket.socket)


clients = {}


class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        data = self.request[0]
        socket = self.request[1]
        logger.debug(f"Got {len(data)} bytes from {self.client_address[0]}")
        if self.client_address not in clients:
            clients[self.client_address] = ClientData(sock=socket)

        cli = clients[self.client_address]

        cli.inbound_buffer += data
        buffer_length = len(cli.inbound_buffer)
        if buffer_length < 4:
            return
        length = int.from_bytes(cli.inbound_buffer[:4], signed=False, byteorder="big")
        if buffer_length < length + 4:
            return
        pck = json.loads(cli.inbound_buffer[4 : 4 + length])
        cli.inbound_buffer = cli.inbound_buffer[4 + length :]

        if pck["t"] == "Connection":
            clients[self.client_address].name = pck["data"]["name"]
            socket.sendto(
                srv_pck.Packet(
                    t="ConfirmConnection",
                    data=srv_pck.ConfirmConnection(id=hash(self.client_address)),
                ).ser(),
                self.client_address,
            )
        elif pck["t"] == "MoveToPosition":
            for soc, c in clients.items():
                if soc == self.client_address:
                    continue
                c.sock.sendto(
                    srv_pck.Packet(
                        t="OMoveToPosition",
                        data=srv_pck.OMoveToPosition(
                            id=hash(self.client_address),
                            new_pos=Position(
                                x=pck["data"]["new_pos"]["x"],
                                y=pck["data"]["new_pos"]["y"],
                            ),
                        ),
                    ).ser(),
                    soc,
                )


def serve() -> None:
    host, port = "0.0.0.0", 25565
    with socketserver.UDPServer((host, port), MyUDPHandler) as srv:
        srv.serve_forever()


def game_loop() -> None:
    while 1:
        time.sleep(1)


if __name__ == "__main__":
    server_thread = threading.Thread(target=serve)
    server_thread.daemon = True
    server_thread.start()
    logger.debug(f"Server loop running in thread: {server_thread.name}")
    game_loop()
