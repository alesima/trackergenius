import socket


class NetworkUtil:
    @staticmethod
    def session(channel: socket.socket) -> str:
        transport = 'U' if isinstance(channel, socket.socket) else 'T'
        return transport + str(channel.getsockname()[1])
