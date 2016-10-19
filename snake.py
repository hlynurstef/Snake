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


    def blitme(self):
        self.head.blitme()
        for block in self.tail:
            block.blitme()


    def set_direction(self, x, y):
        self.x_dir = x
        self.y_dir = y


    def update(self):
        """Update the position of the snake."""
        self.rect.x = self.rect.x + self.scale * self.x_dir
        self.rect.y = self.rect.y + self.scale * self.y_dir
