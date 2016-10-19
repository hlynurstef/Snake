import pygame
from block import Block

class Snake():
    """A class representing the snake."""

    def __init__(self, screen, settings):
        """Initialize the snake."""
        self.screen = screen
        self.settings = settings
        self.tail = []
        self.initialize_snake()
        self.scale = settings.scale
        self.x_dir = 0
        self.y_dir = 0

    def initialize_snake(self):
        """Initialize snake object."""
        self.x = 400
        self.y = 300
        self.head = Block(self.screen, self.settings, self.settings.white,
                          self.x, self.y)
        self.rect = self.head.rect
        self.tail = []
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blitme(self):
        self.head.blitme()
        for block in self.tail:
            block.blitme()


    def set_direction(self, x, y):
        if (x == -1 and not self.moving_right or
            x == 1  and not self.moving_left or
            y == -1 and not self.moving_down or
            y == 1  and not self.moving_up):
            self.x_dir = x
            self.y_dir = y
            self.reset_movement_flags()
            if x == 1:
                self.moving_right = True
            elif x == -1:
                self.moving_left = True
            elif y == 1:
                self.moving_down = True
            elif y == -1:
                self.moving_up = True


    def reset_movement_flags(self):
        """Reset movement flags to False."""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        

    def update(self):
        """Update the position of the snake."""
        self.rect.x = self.rect.x + self.scale * self.x_dir
        self.rect.y = self.rect.y + self.scale * self.y_dir
