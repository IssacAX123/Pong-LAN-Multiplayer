from moving_object import MovingObject

class Player(MovingObject):
    def __init__(self, x, y, width, height, id):
        self.id = id
        super().__init__(x, y, width, height)

    def get_id(self):
        return self.id

    @staticmethod
    def encode_json(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height, "id": self.id}