import pygame as pg

class Body:
    def __init__(self, x, y, file, scale_x, scale_y, angle = 0):
        self.scale_x, self.scale_y = scale_x, scale_y
        self.angle = angle
        self.image = pg.image.load(file).convert_alpha()
        self.image = pg.transform.scale(self.image, (self.scale_x, self.scale_y))
        self.image = pg.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, sc):
        sc.blit(self.image, (self.rect.x, self.rect.y))
