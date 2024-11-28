import pygame as pg
from settings import *
from body import Body
import random as rand

class Plane(Body):
    def __init__(self, x, y, file, scale_x, scale_y, angle = 0):
        super().__init__(x, y, file, scale_x, scale_y, angle)

    def move(self):
        self.rect.y += SPEED
