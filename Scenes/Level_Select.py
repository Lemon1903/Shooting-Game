import sys
import pygame as pg
from .Scene import Scene
from .GameScene import Game
from Scripts.constants import *

class Level_Select(Scene):
    def __init__(self, win):
        super().__init__()
        self.WIN = win

    def draw_window(self):
        self.WIN.fill(WHITE)
        text = SAMPLE_FONT.render("Level Select Scene", 1, 50)
        self.WIN.blit(text, (30, 30))
        pg.display.update()

    def Scene(self):
        key = {pg.K_q: 1, pg.K_w: 2, pg.K_e: 3}
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key in key.keys():
                        Game.level = key[event.key]
                        return "Game"

            self.draw_window()