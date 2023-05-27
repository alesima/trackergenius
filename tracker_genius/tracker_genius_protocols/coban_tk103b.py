from tracker_genius_protocols.socket_server import SocketServer
from tracker_genius_protocols.socket_client import SocketClient


class CobanTk103b(SocketServer):
    def __init__(self, adress, port):
        super().__init__(adress, port)

    def handle_data(self, data: bytes, client: SocketClient):
        pass
