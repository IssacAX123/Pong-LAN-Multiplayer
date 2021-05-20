from moving_object import MovingObject
import math


class Ball(MovingObject):
    def __init__(self, x, y, width, height, x_vel, y_vel):
        self.velocity_vector = [x_vel, y_vel]
        super().__init__(x, y, width, height)

    def enviroment_move(self, player1, player2):
        if (self.x <= player1.getX() + player1.getWidth() and
            player1.getY() <= self.y <= player1.getY() + player1.getHeight()) or \
                self.x >= player2.getX() and \
                player2.getY() <= self.y <= player2.getY() + player2.getHeight():

            self.calcCollisionVelocity()
            self.move()
        else:
            self.move()

    def move(self):
        x = self.velocity_vector[0]
        y = self.velocity_vector[1]
        self.moveX(x)
        self.moveY(y)

    def calcCollisionVelocity(self):
        ball_theta = self.calcDirection()
        self.velocity_vector[0] = (-1 * 3 * 1) / (math.cos(ball_theta))
        self.velocity_vector[1] = (-1 * 3 * 1) / (math.sin(ball_theta))

    def calcDirection(self):
        theta = 0.0
        if self.velocity_vector[0] > 0 and self.velocity_vector[1] > 0:
            theta = (math.atan(abs(self.velocity_vector[1] / self.velocity_vector[0])) / math.pi) * 180
        elif self.velocity_vector[0] < 0 and self.velocity_vector[1] > 0:
            theta = 180 - ((math.atan(abs(self.velocity_vector[1] / self.velocity_vector[0])) / math.pi) * 180)
        elif self.velocity_vector[0] < 0 and self.velocity_vector[1] < 0:
            theta = 270 - ((math.atan(abs(self.velocity_vector[1] / self.velocity_vector[0])) / math.pi) * 180)
        elif self.velocity_vector[0] > 0 and self.velocity_vector[1] < 0:
            theta = 360 - ((math.atan(abs(self.velocity_vector[1] / self.velocity_vector[0])) / math.pi) * 180)
        return theta


