from player import Player
from ball import Ball
import random


class Game:
    def __init__(self, gameId):
        self.ready = False
        self.gameID = gameId
        self.players = [Player(0, 262, 10, 50), Player(858-10, 262, 10, 50)]
        direction =  random.randint(-1,1)
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
        self.players[player] = data

    def getBall(self):
        return self.ball

    def move_ball(self):
        self.ball.enviroment_move(self.players[0], self.players[1])



