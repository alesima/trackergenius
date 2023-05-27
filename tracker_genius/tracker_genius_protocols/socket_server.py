import socket
import threading
from tracker_genius_protocols.socket_client import SocketClient
from tracker_genius_protocols.socket_client_manager import SocketClientManager


class SocketServer:
    def __init__(self, address: str, port: int):
        self.address = address
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_manager = SocketClientManager()
        self.server.bind(self.address, self.port)
        self.server.listen(5)

    def accept_connections(self):
        while True:
            conn, addr = self.server.accept()
            print(f"New connection from {addr}")
            client = SocketClient(conn, addr)
            self.client_manager.add_client(client)
            client_thread = threading.Thread(
                target=self.handle_client, args=(client,))
            client_thread.daemon = True
            client_thread.start()

    def handle_client(self, client: SocketClient):
        while True:
            data = client.conn.recv(1024)
            if not data:
                print(f"Connection closed by {client.addr}")
                self.client_manager.remove_client(client)
                client.conn.close()
                break
            print(f"Received data from {client.addr}: {data.decode('utf-8')}")
            self.handle_data(data, client)

    def handle_data(self, data: bytes, client: SocketClient):
        pass

    def start(self):
        print(f"Server listening on {self.address}:{self.port}")
        accept_thread = threading.Thread(target=self.accept_connections)
        accept_thread.daemon = True
        accept_thread.start()
