
class Game:
    def __init__(self, gameId):
        self.ready = False
        self.gameID = gameId
        self.players = []
        self.points = [0, 0]

    def ready(self):
        self.ready = True

    def movePlayer(self, playerID, velocity):
        self.player[playerID].move(velocity)