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


    def initialize_snake(self):
        """Initialize snake object."""
        self.x = 400
        self.y = 300
        self.x_dir = 0
        self.y_dir = 0
        self.head = Block(self.screen, self.settings, self.settings.white,
                          self.x, self.y)
        self.head_rect = self.head.rect
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


    def intersects(self, x, y, head):
        """
        Checks if x and y intersects with tail. If head = True
        then check if head intersects as well.
        """
        if head:
            if x == self.head_rect.x and y == self.head_rect.y:
                return True
        else:
            for block in self.tail:
                if x == block.rect.x and y == block.rect.y:
                    return True
            return False


    def update(self, ate):
        """Update the position of the snake."""
        x = self.head_rect.x
        y = self.head_rect.y
        self.head_rect.x = self.head_rect.x + self.scale * self.x_dir
        self.head_rect.y = self.head_rect.y + self.scale * self.y_dir
        if not ate:
            if len(self.tail) > 0:
                del self.tail[0]
                self.tail.append(Block(self.screen, self.settings,
                                           self.settings.white, x, y))
        elif ate:
            self.tail.append(Block(self.screen, self.settings,
                                       self.settings.white, x, y))
