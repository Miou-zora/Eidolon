import logging
import capnp
import common.proto.global_capnp as augh
import threading
import time
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        print(f"Got {len(data)} bytes from {self.client_address[0]}")
        socket.sendto(data, self.client_address)


def serve() -> None:
    host, port = "0.0.0.0", 25565
    with socketserver.UDPServer((host, port), MyUDPHandler) as srv:
        srv.serve_forever()


def game_loop() -> None:
    while (1):
        time.sleep(1)


if __name__ == "__main__":
    logging.basicConfig()
    server_thread = threading.Thread(target=serve)
    server_thread.daemon = True
    server_thread.start()
    logging.debug(f"Server loop running in thread: {server_thread.name}")
    game_loop()
