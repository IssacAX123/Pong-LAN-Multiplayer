import socket
from player import Player
import json

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.7"
        self.port = 5556
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        json_data = self.player
        return Player(json_data["x"], json_data["y"], json_data["width"], json_data["height"], json_data["id"])

    def connect(self):
        self.client.connect(self.addr)
        return json.loads((self.client.recv(4096)).decode())

    def send_then_receive(self, data):
        try:
            if isinstance(data, Player):
                player_json_encoder = data.encode_json
                self.client.sendall((json.dumps(data, indent=4, default=player_json_encoder)).encode('utf-8'))
            else:
                self.client.sendall((json.dumps(data, indent=4)).encode('utf-8'))
            return json.loads((self.client.recv(4096)).decode())
        except socket.error as e:
            print(e)
