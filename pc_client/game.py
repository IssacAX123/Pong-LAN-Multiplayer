from player import Player
from ball import Ball
import random
import json


class Game:
    def __init__(self, gameId, players, ball, points):
        self.gameID = gameId
        print(players, type(players))
        self.players = [json.loads(player) for player in players]
        self.ball = json.loads(ball)
        print(points, type(points))
        self.points = json.loads(points)


    def getScore(self):
        return self.points

    def getPlayer(self, player):
        return self.players[player]

    def setPlayer(self, player, data):
        self.players[player].x = data["x"]
        self.players[player].y = data["y"]

    def getBall(self):
        return self.ball



    def encode_json(self, players):
        return {"gameID": players.gameID, "players": [json.dumps(x, indent=4, default=x.encode_json) for x in
                                                      self.players],
                "ball": json.dumps(self.ball, indent=4, default=self.ball.encode_json),
                "points": json.dumps(players.points, indent=4)}




