# enemy_bullet.py
import pygame as pg

class EnemyBullet:
    def __init__(self, x, y, player_x, player_y):
        self.x = x
        self.y = y
        self.player_x = player_x
        self.player_y = player_y
        self.speed = 8
        self.radius = 5
    
    def update(self):
        # Move the bullet towards the player's position
        dx = self.player_x - self.x
        dy = self.player_y - self.y
        distance = max(1, pg.math.Vector2(dx, dy).length())
        direction = pg.math.Vector2(dx / distance, dy / distance)
        self.x += direction.x * self.speed
        self.y += direction.y * self.speed
    
    def render(self, screen):
        # Render the bullet on the screen
        pg.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)
