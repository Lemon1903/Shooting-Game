import pygame as pg
from Scenes.GameScene import Game
from Scenes.Level_Select import Level_Select
from Scripts.constants import *

WIN = pg.display.set_mode((SCREEN_W, SCREEN_H))
pg.display.set_caption("Shooting Game 1.0")

def main():
    scenes = {
        "Game": Game(WIN),
        "Level Select": Level_Select(WIN)
    }
    scene = "Game"
    
    while scene in scenes.keys():
        scene = scenes[scene].Scene()

if __name__ == "__main__":
    main()