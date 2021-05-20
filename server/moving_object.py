class MovingObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def moveX(self, velocity):
        self.x += velocity

    def moveY(self, velocity):
        self.y += velocity

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get_draw_details(self):
        return (self.x, self.y, self.width, self.height)