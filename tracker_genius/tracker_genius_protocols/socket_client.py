import socket


class SocketClient:
    def __init__(self, conn: socket.socket, addr: str):
        self.conn = conn
        self.addr = addr

    def send(self, message):
        self.conn.send(message)
