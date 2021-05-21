from player import Player
from ball import Ball
import random
import json


class Game:
    def __init__(self, gameId):
        self.ready = False
        self.gameID = gameId
        self.players = [Player(0, 262, 10, 50, 0), Player(858-10, 262, 10, 50, 1)]
        direction = random.randint(-1,1)
        self.ball = Ball(429-5, 262-25, 5, 5, direction * 5, 0)
        self.points = [0, 0]

    def revert_ready(self):
        self.ready = not self.ready

    def connected(self):
        return self.ready

    def movePlayer(self, playerID, velocity):
        self.players[playerID].moveY(velocity)

    def reinitialize_ball(self):
        self.ball.x = 429-5
        self.ball.y = 262-25
        direction = random.randint(-1, 1)
        self.ball.x_vel = direction * 5
        self.ball.y_vel = 0

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
        self.ball.enviroment_move(self.players[0], self.players[1])

    def update_scores(self):
        pass

    def encode_json(self, players):
        return {"gameID": players.gameID, "players": [json.dumps(x, indent=4, default=x.encode_json) for x in
                                                      self.players],
                "ball": json.dumps(self.ball, indent=4, default=self.ball.encode_json),
                "points": players.points, "connected": str(players.ready).lower()}




