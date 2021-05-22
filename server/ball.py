from moving_object import MovingObject
import math
import random

class Ball(MovingObject):
    def __init__(self, x, y, width, height, x_vel, y_vel):
        self.velocity_vector = [x_vel, y_vel]
        super().__init__(x, y, width, height)

    def enviroment_move(self, player1, player2):
        print("enviroment_move", self.x, self.y, self.velocity_vector)
        if (self.x + self.velocity_vector[0] <= player1.getX() + player1.getWidth() and (
                player1.getY() <= self.y + self.velocity_vector[1] <= player1.getY() + player1.getHeight())):
            self.calcCollisionVelocityWithPlayer(player1.y_velocity)
            self.move()
            return False, None
        elif (self.x + self.velocity_vector[0] >= player2.getX() and (
                    player2.getY() <= self.y + self.velocity_vector[1] <= player2.getY() + player2.getHeight())):
            self.calcCollisionVelocityWithPlayer(player2.y_velocity)
            self.move()
            return False, None
        elif (self.y + self.velocity_vector[1] <= 5 and (30 <= self.x + self.velocity_vector[0] <= 828)) or (
                            self.y + self.velocity_vector[1] >= 520 and (30 <= self.x + self.velocity_vector[0] <= 828)):
            self.calcCollisionVelocityWithBorder(0)
            self.move()
            return False, None
        elif self.x + self.velocity_vector[0] > 858:
            self.reinitialize_ball()
            self.move()
            return True, player1
        elif self.x + self.velocity_vector[0] < 0:
            self.reinitialize_ball()
            self.move()
            return True, player2
        else:
            print("normal move", self.x, self.y, self.velocity_vector)
            self.move()
            return False, None


    def move(self):
        x = self.velocity_vector[0]
        y = self.velocity_vector[1]
        self.moveX(x)
        self.moveY(y)

    def calcCollisionVelocity_bckp(self):
        ball_theta = self.calcDirection()
        print(type(ball_theta), type(math.radians(ball_theta)))
        print(ball_theta != math.radians(0.0))
        print("------------------------------------")
        print("------------------------------------")
        print("ball theta", ball_theta, (ball_theta/math.pi)*180)
        print("------------------------------------")
        print("------------------------------------")
        if ball_theta != math.radians(90.0) and ball_theta != math.radians(270.0):
            self.velocity_vector[0] = (-1 * 3 * 1) / (math.cos(ball_theta))
        else:
            self.velocity_vector[0] = self.velocity_vector[0] * -0.75
        if ball_theta != math.radians(0.0) and ball_theta != math.radians(180.0) and ball_theta != math.radians(360.0):
            self.velocity_vector[1] = (-1 * 3 * 1) / (math.sin(ball_theta))
        else:
            self.velocity_vector[1] = self.velocity_vector[1] * -0.75

        print(ball_theta, self.velocity_vector[0], self.velocity_vector[1])

    def calcCollisionVelocityWithPlayer(self, surface_y_vel):
        self.velocity_vector[0]  *= -1

    def calcCollisionVelocityWithBorder(self, surface_y_vel):
        self.velocity_vector[1] *= -1


    def calcDirection(self):
        theta = 0.0
        if self.velocity_vector[0] > 0 and self.velocity_vector[1] > 0:
            theta = (math.atan(self.velocity_vector[1] / self.velocity_vector[0]))
        elif self.velocity_vector[0] < 0 and self.velocity_vector[1] > 0:
            theta = math.pi - ((math.atan(self.velocity_vector[1] / self.velocity_vector[0])))
        elif self.velocity_vector[0] < 0 and self.velocity_vector[1] < 0:
            theta = 1.5*math.pi - (math.atan(self.velocity_vector[1] / self.velocity_vector[0]))
        elif self.velocity_vector[0] > 0 and self.velocity_vector[1] < 0:
            theta = 2*math.pi - ((math.atan(self.velocity_vector[1] / self.velocity_vector[0])))
        return theta

    def reinitialize_ball(self):
        self.x = 429-5
        self.y = 262-25
        direction = [-1, 1]
        option = random.randint(0, 1)
        self.velocity_vector[0] = direction[option] * 3
        option = random.randint(0, 1)
        self.velocity_vector[1] = direction[option] * 1


