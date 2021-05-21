from moving_object import MovingObject
import pygame
pygame.font.init()
font = pygame.font.SysFont("comicsans", 40)

class Player(MovingObject):
    def __init__(self, x, y, width, height, id):
        self.id = id
        self.wins = 0
        super().__init__(x, y, width, height)

    def draw_win(self, win, playerID):
        text = font.render(str(self.wins), 1, (255, 255, 255))
        if playerID == 0:
            win.blit(text, (420, 5))
        else:
            win.blit(text, (438, 5))

    def get_id(self):
        return self.id

    @staticmethod
    def encode_json(self):
        return {"x": self.x, "y": self.y, "id": self.id}



