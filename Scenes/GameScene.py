import sys, math
import pygame as pg
from .Scene import Scene
from Scripts.player import Player
from Scripts.enemy import Enemy
from Scripts.bullet import Bullet
from Scripts.weapon_menu import Weapon_Menu
from Scripts.constants import *

class Game(Scene):
    clock = pg.time.Clock()
    current_time = pg.time.get_ticks()
    previous_shot_time, previous_spawn_time = 0, 0
    level = 1

    def __init__(self, win):
        super().__init__()

        self.WIN = win
        self.wall = pg.Rect(0, 0, SCREEN_W, SCREEN_H)
        self.wall_thickness = 20
        self.angle_to_mouse = 0
        self.enemy_speed = 2
        self.spawn_time = 2000
        self.player = Player(SCREEN_W/2 - PLAYER_W/2, SCREEN_H/2 - PLAYER_H/2)
        self.weapon_menu = Weapon_Menu()
        self.enemies = pg.sprite.Group()
        self.bullets = pg.sprite.Group()

    def draw_window(self):
        self.WIN.fill(GRAY4)
        self.player.draw(self.WIN)
        self.bullets.draw(self.WIN)
        self.enemies.draw(self.WIN)
        
        if self.weapon_menu.is_open:
            self.weapon_menu.draw(self.WIN, self.player.rect.center)
        else:
            self.spawn_enemies()
            self.handle_player_movement()
            self.player.update(self.WIN, self.angle_to_mouse)
            self.bullets.update(self.wall.w, self.wall.h) 
            self.enemies.update(self.WIN, self.player)

        self.show_score()
        pg.draw.rect(self.WIN, BLACK, self.wall, self.wall_thickness)
        pg.display.update()

    def handle_player_movement(self):
        keys_pressed = pg.key.get_pressed()
        if (keys_pressed[pg.K_a] and not self.player.have_object_left
            and self.player.rect.left > self.wall_thickness):
            self.player.move_left()
        if (keys_pressed[pg.K_d] and not self.player.have_object_right
            and self.player.rect.right < self.wall.w - self.wall_thickness):
            self.player.move_right()
        if (keys_pressed[pg.K_w] and not self.player.have_object_top
            and self.player.rect.top > self.wall_thickness):
            self.player.move_up()
        if (keys_pressed[pg.K_s] and not self.player.have_object_bottom
            and self.player.rect.bottom < self.wall.h - self.wall_thickness):
            self.player.move_down()

    def handle_bullets(self):
        for bullet in self.bullets:
            for enemy in reversed(self.enemies.sprites()):
                if bullet.rect.colliderect(enemy):
                    enemy.health.w -= 10
                    bullet.kill()
                    break

    def spawn_bullets(self):
        if (self.player.is_shooting and not self.weapon_menu.is_open 
            and Game.current_time - Game.previous_shot_time >= 150):
            bullet = Bullet(self.player.rect.center, self.angle_to_mouse)
            self.bullets.add(bullet)
            Game.previous_shot_time = Game.current_time
        
    def spawn_enemies(self):
        if Game.current_time - Game.previous_spawn_time >= self.spawn_time:
            enemy = Enemy(self.enemy_speed)
            self.enemies.add(enemy)
            Game.previous_spawn_time = Game.current_time

    def show_game_over(self):
        game_over = GAME_OVER_FONT.render("Game Over", 1, BLACK)
        self.WIN.blit(game_over, (SCREEN_W/2 - game_over.get_width()/2, SCREEN_H/2 - game_over.get_height()/2))
        pg.display.update()

    def show_score(self):
        score = SCORE_FONT.render(f"Score: {self.player.score}", 1, BLACK)
        self.WIN.blit(score, (self.wall_thickness + 10, self.wall_thickness + 10))

    def get_angle(self, mouse_pos):
        delta = mouse_pos - pg.Vector2(self.player.rect.center)
        self.angle_to_mouse = -round(math.degrees(math.atan2(delta.y, delta.x)))

    def update_spawn_time(self):
        if Game.current_time % 25000 <= 30:
            self.spawn_time -= 200

    def update_enemy_speed(self):
        if Game.current_time % 60000 <= 30:
            self.enemy_speed += 0.2

    def Scene(self):
        while True:
            Game.clock.tick(60)
            Game.current_time = pg.time.get_ticks()
            mouse_pos = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.player.is_shooting = True
                if event.type == pg.MOUSEBUTTONUP: 
                    self.player.is_shooting = False
                if event.type == pg.MOUSEMOTION:
                    self.get_angle(mouse_pos)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.weapon_menu.open()
                    if event.key == pg.K_RETURN:
                        self.__init__(self.WIN)
                        return "Game"

            if self.player.health.w <= 0:
                self.show_game_over()
            else:
                self.update_enemy_speed()
                self.update_spawn_time()
                self.handle_bullets()
                self.spawn_bullets()
                self.draw_window()