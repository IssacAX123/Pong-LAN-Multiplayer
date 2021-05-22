from player import Player
from ball import Ball
import random
import json


class Game:
    def __init__(self, gameId):
        self.ready = False
        self.gameID = gameId
        self.players = [Player(5, 262, 25, 95, 0), Player(858-30, 262, 25, 95, 1)]
        direction = [-1, 1]
        self.ball = Ball(429-5, 262-25, 10, 10, direction[random.randint(0, 1)] * 4, direction[random.randint(0, 1)] * 1)
        self.points = [0, 0]

    def revert_ready(self):
        self.ready = not self.ready

    def connected(self):
        return self.ready

    def movePlayer(self, playerID, velocity):
        self.players[playerID].moveY(velocity)

    def getScore(self):
        return self.points

    def getPlayer(self, player):
        return self.players[player]

    def setPlayer(self, player, data):
        print("before", self.players[player].x, self.players[player].y)
        self.players[player].x = data["x"]
        self.players[player].y = data["y"]
        print("after", self.players[player].x, self.players[player].y)

    def getBall(self):
        return self.ball

    def move_ball(self):
        scored, player = self.ball.enviroment_move(self.players[0], self.players[1])
        if scored:
            if player.id == 0:
                self.points[0] += 1
            elif player.id == 1:
                self.points[1] += 1



    def encode_json(self, players):
        return {"gameID": players.gameID, "players": [json.dumps(x, indent=4, default=x.encode_json) for x in
                                                      self.players],
                "ball": json.dumps(self.ball, indent=4, default=self.ball.encode_json),
                "points": json.dumps(players.points, indent=4), "connected": str(players.ready).lower()}




