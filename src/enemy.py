import pygame as pg
from entity import Entity
import random
from enemy_bullet import EnemyBullet

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50  # Set the width of the player
        self.height = 50  # Set the height of the player
        self.speed = 1
        self.health = 10

        self.shoot_cooldown = 60  # Cooldown between shots (in frames)
        self.shoot_timer = 0
      
    
    def update(self, player_x, player_y):
        # Move towards the player
        dx = player_x - self.x
        dy = player_y - self.y
        distance = max(1, pg.math.Vector2(dx, dy).length())
        direction = pg.math.Vector2(dx / distance, dy / distance)
        self.x += direction.x * self.speed
        self.y += direction.y * self.speed

        # Shoot at the player
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_cooldown:
            self.shoot_timer = 0
            bullet = EnemyBullet(self.x + self.width // 2, self.y + self.height // 2, player_x, player_y)
            return bullet
    
    def render(self, screen):
        # Render enemy on the screen
        pg.draw.rect(screen, (255, 0, 0), pg.Rect(self.x, self.y, self.width, self.height))  # Red rectangle representing the enemy

    def check_border_collision(self, screen_width, screen_height):
        # Prevent player from going out of the screen
        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))

        