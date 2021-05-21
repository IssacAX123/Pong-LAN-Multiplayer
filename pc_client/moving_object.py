import pygame
import json

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

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, data):
        self.x = data

    def setY(self, data):
        self.y = data

    @staticmethod
    def encode_json(self):
        return {"x": self.x, "y": self.y}

