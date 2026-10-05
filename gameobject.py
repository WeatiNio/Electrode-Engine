import pygame as pg

class GameObject:
    def __init__(self, x=0, y=0, width=100, height=100, colour="#ffffff"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.colour = colour

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height

    def draw(self, screen):
        pg.draw.rect(screen, self.colour, self.rect)