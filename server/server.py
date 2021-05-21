import threading
import socket
from game import Game
import json
import sys
import traceback

SERVER = "192.168.1.7"
PORT = 5556
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
    global idCount
    print("threaded")
    print(games[gameID].getPlayer(player))
    player_to_send = games[gameID].getPlayer(player)
    player_json_encoder = games[gameID].getPlayer(player).encode_json
    connection.sendall((json.dumps(player_to_send, indent=4, default=player_json_encoder)).encode('utf-8'))
    while True:
        try:
            json_data = None
            try:
                json_data = (json.loads(connection.recv(4096)))
                print("data ", json_data, type(json_data))
            except Exception as e:
                print(e)
            if not json_data:
                games[gameID].revert_ready()
                break
            else:
                games[gameID].setPlayer(player, json_data)
                games[gameID].move_ball()
            game_json_encoder = games[gameID].encode_json
            connection.sendall((json.dumps(games[gameID], indent=4, default=game_json_encoder)).encode("utf-8"))
        except Exception as e:
            print(e)
            traceback.print_exc()
            break

    try:
        del games[gameID]
        print("Lost Connection", " Closing game ", gameID)
    except:
        pass
    idCount -= 1
    connection.close()


while True:
    connection, address = s.accept()
    print(f"Connected to {address}")
    idCount += 1
    gameID = (idCount - 1) // 2
    if idCount % 2 == 1:
        player = 0
        games[gameID] = Game(gameID)
        print("created game ", gameID)
    else:
        games[gameID].revert_ready()
        player = 1

    threading.Thread(target=threaded_client, args=(connection, player, gameID)).start()
