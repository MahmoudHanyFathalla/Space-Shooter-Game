import pygame as pg
from entity import Entity
from bullet import Bullet

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50  # Set the width of the player
        self.height = 50  # Set the height of the player
        self.speed = 5
        self.bullets = []  # List to store bullets
        self.health = 100
    
    def update(self):
        # Update player state (e.g., movement)
        for bullet in self.bullets:
            bullet.update()
        
    def render(self, screen):
        # Render player on the screen
        pg.draw.rect(screen, (0, 255, 0), pg.Rect(self.x, self.y, self.width, self.height))  # Green rectangle representing the player
        for bullet in self.bullets:
            bullet.render(screen)

    def shoot(self, direction):
        # Create a bullet and add it to the list of bullets
        bullet = Bullet(self.x + self.width // 2, self.y + self.height // 2, direction)
        self.bullets.append(bullet) 
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy


    def check_border_collision(self, screen_width, screen_height):
        # Prevent player from going out of the screen
        self.x = max(0, min(self.x, screen_width - self.width))
        self.y = max(0, min(self.y, screen_height - self.height))

        