# bullet.py
import pygame as pg

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction  # Direction of the bullet (up, down, left, right)
        self.speed = 10  # Speed of the bullet
        self.radius = 5  # Radius of the bullet
    
    def update(self):
        # Move the bullet in its direction
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed
    
    def render(self, screen):
        # Render the bullet on the screen
        pg.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
