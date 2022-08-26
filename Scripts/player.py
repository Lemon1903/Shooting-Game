import pygame as pg
from .constants import *

class Player(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        # player
        self.shooting_image = pg.transform.smoothscale(pg.image.load(
            "Assets/character_shooting.png"), (PLAYER_W, PLAYER_H))
        self.idle_image = pg.transform.smoothscale(pg.image.load(
            "Assets/character_idle.png"), (PLAYER_W, PLAYER_H))
        self.image = self.idle_image
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)
        self.health = pg.Rect(self.rect.left, self.rect.top - 20, 50, 10)
        self.empty_health = pg.Rect(self.rect.left, self.rect.top - 20, 50, 10)
        self.velocity = 3
        self.score = 0
        self.is_shooting = False
        # check if there's an ovject in sides
        self.have_object_left = False
        self.have_object_right = False
        self.have_object_top = False
        self.have_object_bottom = False

    # ===== player movement =====
    def move_left(self):
        self.rect.x -= self.velocity

    def move_right(self):
        self.rect.x += self.velocity

    def move_up(self):
        self.rect.y -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity

    # ===== updating player sprite =====
    def draw(self, parent):
        parent.blit(self.image, self.rect)

    def rotate(self, angle, img):
        self.image = pg.transform.rotate(img, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, parent, angle):
        # rotate image
        img = self.shooting_image if self.is_shooting else self.idle_image
        self.rotate(angle, img)
        # default object checking back to false
        self.have_object_left = False
        self.have_object_right = False
        self.have_object_bottom = False
        self.have_object_top = False
        # updates health location
        self.health.topleft = (self.rect.left, self.rect.top - 20)
        self.empty_health.topleft = self.health.topleft
        pg.draw.rect(parent, GRAY1, self.empty_health)
        pg.draw.rect(parent, GREEN, self.health)