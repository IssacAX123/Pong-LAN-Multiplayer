import threading
import socket
from game import Game
import pickle

SERVER = "192.168.1.7"
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((SERVER, PORT))
except socket.error as e:
    print(e)

s.listen()
connected_clients = set()
games = {}
idCount = 0

def threaded_client(connection, player, gameID):
    connection.send(pickle.dumps(games[gameID].getPlayer(player)))
    while True:
        data = None
        try:
            data = pickle.loads(connection.recv(4096))
        except Exception as e:
            print(e)
        if not data:
            games[gameID].revert_ready()
            break
        else:
            games[gameID].setPlayer(player, data)
            games[gameID].move_ball()

        connection.sendall(pickle.dumps(games[gameID]))



while True:
    connection, address = s.accept()
    print(f"Connected to {address}")
    idCount += 1
    gameID = (idCount-1) - 2
    if idCount % 2 == 1:
        player = 0
        games[gameID] = Game(gameID)
        print("created game ", gameID)
    else:
        games[gameID].revert_ready()
        player = 1

    threading.Thread(target=threaded_client, args=(connection, player, gameID))

