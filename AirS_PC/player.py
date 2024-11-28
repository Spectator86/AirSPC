import pygame as pg
from settings import *
from body import Body

class Player(Body):
    def __init__(self, x, y, file, speed, scale_x = 100, scale_y = 100, angle = 0):
        super().__init__(x, y, file, scale_x, scale_y, angle)
        self.speed = speed

    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[pg.K_d] and self.rect.x + self.scale_x < WIDTH - 10:
            self.rect.x += self.speed
