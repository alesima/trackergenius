class SocketClientManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.clients = []
        return cls._instance
    
    def add_client(self, client):
        self.clients.appennd(client)

    def remove_client(self, client):
        self.cients.remove(client)

    def send_message(self, client_address, message):
        for client in self.clients:
            if client.address == client_address:
                client.send(message)