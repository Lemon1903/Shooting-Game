import pygame as pg
import math
from .constants import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, player_center, angle):
        super().__init__()

        self.angle = angle
        self.speed = 7
        self.image = pg.transform.rotate(pg.transform.scale(
            pg.image.load("Assets/bullet.png"), (BULLET_W, BULLET_H)), angle)
        self.dx = math.cos(math.radians(-angle))
        self.dy = math.sin(math.radians(-angle))
        self.pos_x = player_center[0] + self.dx * (PLAYER_W - 20)
        self.pos_y = player_center[1] + self.dy * (PLAYER_H - 20)
        self.rect = self.image.get_rect(x=self.pos_x, y=self.pos_y)
        self.vector = pg.Vector2(self.dx * self.speed, self.dy * self.speed)

    def update(self, wall_w, wall_h):
        if (self.rect.left <= 0 or self.rect.right >= wall_w
            or self.rect.top <= 0 or self.rect.bottom >= wall_h):
            self.kill()

        self.rect.topleft += self.vector.xy