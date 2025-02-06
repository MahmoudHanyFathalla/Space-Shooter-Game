# gift.py

import pygame as pg
import random
import pygame.event as pg_event

class Gift:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.width = 20  # Width of the gift
        self.height = 20  # Height of the gift
        self.frequency = 600  # Appearance frequency in frames (10 seconds at 60 FPS)
        self.timer = 0  # Timer to track when to spawn the next gift
        self.gifts = []  # List to store active gifts
        self.visible = False  # Flag to track if the gift is currently visible
    
    def update(self):
        # Increment the timer
        self.timer += 1
        # Check if it's time to spawn a new gift
        if self.timer >= self.frequency:
            self.timer = 0  # Reset the timer
            self.spawn_gift()  # Spawn the gift
    
    def spawn_gift(self):
        # Randomly determine the position of the gift
        x = random.randint(0, self.screen_width - self.width)
        y = random.randint(0, self.screen_height - self.height)
        self.gifts.append((x, y))  # Add the new gift position to the list of active gifts
    
    def render(self, screen):
        # Render all active gifts on the screen
        for gift in self.gifts:
            pg.draw.rect(screen, (255, 255, 0), pg.Rect(gift[0], gift[1], self.width, self.height))

    def check_player_collision(self, player_x, player_y, player_width, player_height):
        # Check collision between player and gifts
        player_rect = pg.Rect(player_x, player_y, player_width, player_height)
        for gift_pos in self.gifts:
            gift_rect = pg.Rect(gift_pos[0], gift_pos[1], self.width, self.height)
            if player_rect.colliderect(gift_rect):
                self.gifts.remove(gift_pos)
                # Emit event to signal that the gift has been collected
                pg_event.post(pg_event.Event(pg.USEREVENT, {"gift_collected": True}))
