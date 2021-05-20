from moving_object import MovingObject


class Ball(MovingObject):
    def __init__(self, x, y, width, height):
        self.wins = 0
        super().__init__(x, y, width, height)

    def checkCollision(self, player1, player2):
        if self.x <= player1.getX() + player1.getWidth() or self.x >= player2.getX():
            return True
        else:
            return False
