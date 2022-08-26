import pygame as pg

pg.init()
# ===== colors =====
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 50)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
GRAY1 = (212, 212, 212)
GRAY4 = (99, 99, 99)
# ===== sizes =====
SCREEN_W, SCREEN_H = 800, 600
PLAYER_W, PLAYER_H = 45, 45
BULLET_W, BULLET_H = 5, 5
WP_MENU_W, WP_MENU_H = 250, 250
# ===== fonts =====
SAMPLE_FONT = pg.font.SysFont("Arial", 50)
GAME_OVER_FONT = pg.font.Font("Assets/fonts/ThaleahFat.ttf", 100)
SCORE_FONT = pg.font.Font("Assets/fonts/ThaleahFat.ttf", 50)