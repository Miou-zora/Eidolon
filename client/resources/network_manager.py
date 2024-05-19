from common.engine.resource import Resource
from common.engine.engine import Engine
from common.proto.server_packets import ConfirmConnection, Packet

import common.proto.server_packets as srv_pck

from threading import Thread, Lock
import socket
import random
import json


class NetworkManager(Resource):
    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.connected: bool = False
        self.client_id: int = 0
        self._network_thread: Thread = Thread(target=self._run)
        self._network_thread.daemon = True
        self._inbound_queue_lock: Lock = Lock()
        self._inbound_queue: list[Packet] = list()
        self._server_ip = "127.0.0.1"
        self._server_port = 25565
        self._client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._client_port = random.randint(6000, 10000)
        self._client_ip = "0.0.0.0"
        self._client_socket.bind((self._client_ip, self._client_port))
        self._inbound_buffer: bytes = bytes()

    def _run(self) -> None:
        while True:
            data, addr = self._client_socket.recvfrom(2048)
            # TODO: Check the data comes from the server
            self._inbound_buffer += data
            buffer_length = len(self._inbound_buffer)
            if buffer_length < 4:
                continue
            length = int.from_bytes(self._inbound_buffer[:4], signed=False)
            if buffer_length < length + 4:
                continue
            data = json.loads(self._inbound_buffer[4 : 4 + length])
            self._inbound_buffer = self._inbound_buffer[4 + length :]
            if data["t"] == "ConfirmConnection":
                with self._inbound_queue_lock:
                    self._inbound_queue.append(
                        Packet(
                            t=data["t"],
                            data=ConfirmConnection(id=data["data"]["id"]),
                        )
                    )

    def _send_packet(self, pck: Packet) -> None:
        self._client_socket.sendto(pck.ser(), (self._server_ip, self._server_port))

    def launch(self) -> None:
        self._network_thread.start()

    def connect(self, name: str) -> None:
        self._send_packet(
            Packet(
                t="Connection",
                data=srv_pck.Connection(name=name),
            )
        )

    def get_inbound_packets(self) -> list[Packet]:
        with self._inbound_queue_lock:
            packets = self._inbound_queue
            self._inbound_queue = list()
            return packets
