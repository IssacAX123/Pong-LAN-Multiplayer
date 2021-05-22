from moving_object import MovingObject

class Player(MovingObject):
    def __init__(self, x, y, width, height, id):
        self.id = id
        self.y_velocity = 0
        super().__init__(x, y, width, height)

    def get_id(self):
        return self.id

    def moveY(self, velocity):
        if 520 > self.y + velocity > 5:
            self.y += velocity
            self.y_velocity = velocity

    @staticmethod
    def encode_json(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height, "id": self.id}