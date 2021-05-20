from moving_object import MovingObject

class Player(MovingObject):
    def __init__(self, x, y, width, height):
        self.wins = 0
        super().__init__(x, y, width, height)

    def win(self):
        self.wins += 1