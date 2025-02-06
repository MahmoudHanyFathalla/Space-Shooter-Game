# game.py (updated)

import pygame as pg
from player import Player
from enemy import Enemy
from gift import Gift
from helper import Helper
import os
import random
from enemy_bullet import EnemyBullet
import pygame.event as pg_event

class Game:
    def __init__(self):
        self.player = Player(100, 100)
        self.enemies = []
        self.enemy_bullets = []  
        self.screen_width = 800
        self.screen_height = 600
        self.enemy_spawn_rate = 1  
        self.spawn_timer = 0
        self.gift = Gift(self.screen_width, self.screen_height)
        self.helpers = []  # Initialize list to store helpers
    
    def update(self):
        if self.player:  
            self.player.update()
            player_x, player_y = self.player.x, self.player.y  
            self.gift.update()  
            self.gift.check_player_collision(player_x, player_y, self.player.width, self.player.height)
            for enemy in self.enemies:
                bullet = enemy.update(player_x, player_y)
                if bullet:
                    self.enemy_bullets.append(bullet)

            for helper in self.helpers:
                helper.update(self.enemy_bullets)  # Update all helpers with enemy bullets

            self.player.check_border_collision(self.screen_width, self.screen_height)
            for enemy in self.enemies:
                enemy.check_border_collision(self.screen_width, self.screen_height)

            for bullet in self.player.bullets:
                for enemy in self.enemies:
                    if self.check_collision(bullet, enemy):
                        enemy.health -= 10
                        if enemy.health <= 0:
                            self.enemies.remove(enemy)
                        self.player.bullets.remove(bullet)
                        break

            for bullet in self.enemy_bullets:
                if self.check_collision(bullet, self.player):
                    self.player.health -= 10
                    if self.player.health <= 0:
                        self.player = None 
                    self.enemy_bullets.remove(bullet)
                    break

        self.spawn_timer += 1
        if self.spawn_timer >= 500:  
            self.spawn_timer = 0
            for _ in range(self.enemy_spawn_rate):
                self.enemies.append(Enemy(random.randint(0, self.screen_width), random.randint(0, self.screen_height)))
            self.enemy_spawn_rate += 1  

    def render(self, screen):
        screen.blit(self.background, (0, 0))  
        self.player.render(screen)
        for enemy in self.enemies:
            enemy.render(screen)
        for bullet in self.enemy_bullets:  
            bullet.render(screen)
        self.gift.render(screen)
        for helper in self.helpers:
            helper.render(screen)

    def run(self):
        pg.init()  
        clock = pg.time.Clock()
        screen = pg.display.set_mode((self.screen_width, self.screen_height))

        current_dir = os.path.dirname(__file__)
        background_path = os.path.join(current_dir, "..", "assets", "images", "background.png")
        background_image = pg.image.load(background_path)
        self.background = pg.transform.scale(background_image, (self.screen_width, self.screen_height))

        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.player.shoot("up")
                    elif event.key == pg.K_s:
                        self.player.shoot("down")
                    elif event.key == pg.K_a:
                        self.player.shoot("left")
                    elif event.key == pg.K_d:
                        self.player.shoot("right")
                elif event.type == pg.USEREVENT:
                    if "gift_collected" in event.dict and event.dict["gift_collected"]:
                        # Create a new helper when a gift is collected
                        new_helper = Helper(random.randint(0, self.screen_width), random.randint(0, self.screen_height))
                        self.helpers.append(new_helper)

            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                self.player.move(-5, 0)
            if keys[pg.K_RIGHT]:
                self.player.move(5, 0)
            if keys[pg.K_UP]:
                self.player.move(0, -5)
            if keys[pg.K_DOWN]:
                self.player.move(0, 5)            

            self.update()
            self.render(screen)

            pg.display.flip()
            clock.tick(60)

        pg.quit()

    def check_collision(self, obj1, obj2):
        return (obj1.x < obj2.x + obj2.width and obj1.x + obj1.radius > obj2.x and
                obj1.y < obj2.y + obj2.height and obj1.y + obj1.radius > obj2.y)

if __name__ == "__main__":
    game = Game()
    game.run()
