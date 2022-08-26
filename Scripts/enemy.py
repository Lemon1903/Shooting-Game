import pygame as pg
import random, math
from .constants import *

class Enemy(pg.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()

        # enemy sprite
        self.speed = speed
        self.image = pg.Surface((50, 50))
        self.image.fill(BLUE)
        # random starting positions
        angle = random.uniform(-3, 3)
        pos_x = math.cos(angle) * SCREEN_W/2
        pos_y = math.sin(angle) * SCREEN_H/2
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)
        self.health = pg.Rect(self.rect.left, self.rect.top - 15, 50, 10)
        self.empty_health = pg.Rect(self.rect.left, self.rect.top - 15, 50, 10)

    # ===== updates enemy sprite =====
    def update(self, parent, player):
        # solve for the vector
        delta = player.rect.center - pg.Vector2(self.rect.center)
        angle = math.atan2(delta.y, delta.x)
        vector = pg.Vector2(self.speed * math.cos(angle), self.speed * math.sin(angle))

        # delete sprite at no health
        if self.health.w <= 0:
            player.score += 100
            self.kill()
        # check for collision with the player
        elif not self.rect.colliderect(player.rect):
            self.rect.topleft += vector.xy
            self.health.topleft += vector.xy
            self.empty_health.topleft = self.health.topleft
        else:
            player.health.w -= 1
            if abs(self.rect.left - player.rect.right) <= 20:
                player.have_object_right = True
            if abs(self.rect.right - player.rect.left) <= 20:
                player.have_object_left = True
            if abs(self.rect.top - player.rect.bottom) <= 20:
                player.have_object_bottom = True
            if abs(self.rect.bottom - player.rect.top) <= 20:
                player.have_object_top = True

        pg.draw.rect(parent, GRAY1, self.empty_health)
        pg.draw.rect(parent, RED, self.health)