# helper.py (updated)
import pygame as pg
from entity import Entity

class Helper(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50  # Set the width of the helper
        self.height = 50  # Set the height of the helper
        self.speed = 1
        self.health = 10
        self.bullets_taken = 0  # Number of bullets taken by the helper
        self.max_bullets = 10  # Maximum number of bullets the helper can take

    def update(self, enemy_bullets):
        # Move towards enemy bullets
        if enemy_bullets and self.bullets_taken < self.max_bullets:
            closest_bullet = min(enemy_bullets, key=lambda bullet: ((bullet.x - self.x)**2 + (bullet.y - self.y)**2))
            dx = closest_bullet.x - self.x
            dy = closest_bullet.y - self.y
            distance = max(1, pg.math.Vector2(dx, dy).length())
            direction = pg.math.Vector2(dx / distance, dy / distance)
            self.x += direction.x * self.speed
            self.y += direction.y * self.speed

            # Check collision with enemy bullets and take them
            for bullet in enemy_bullets:
                if self.check_collision(self, bullet):
                    self.bullets_taken += 1
                    enemy_bullets.remove(bullet)  # Remove the bullet from the enemy bullets list
                    if self.bullets_taken >= self.max_bullets:
                        self.health = 0  # Set health to 0 to trigger removal

    def render(self, screen):
        # Render helper on the screen if it's alive
        if self.health > 0:
            pg.draw.rect(screen, (0, 0, 255), pg.Rect(self.x, self.y, self.width, self.height))  # Blue rectangle representing the helper

    def check_collision(self, obj1, obj2):
        # Simple AABB collision detection
        return (obj1.x < obj2.x + obj2.radius and obj1.x + obj1.width > obj2.x and
                obj1.y < obj2.y + obj2.radius and obj1.y + obj1.height > obj2.y)
