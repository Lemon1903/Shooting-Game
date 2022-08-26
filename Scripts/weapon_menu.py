import pygame as pg

from Scripts.constants import PLAYER_H, PLAYER_W, WP_MENU_H, WP_MENU_W

class Weapon_Menu(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.transform.smoothscale(pg.image.load(
            "Assets/weapon_menu.png"), (WP_MENU_W, WP_MENU_H))
        self.rect = self.image.get_rect()
        self.is_open = False

    def open(self):
        self.is_open = not self.is_open

    def draw(self, parent, player_center):
        self.rect.center = player_center
        parent.blit(self.image, self.rect)