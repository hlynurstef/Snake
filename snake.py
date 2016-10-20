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
        self.directions = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}


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
        self.movement = {'up': False, 'down': False, 'left': False, 'right': False}


    def blitme(self):
        self.head.blitme()
        for block in self.tail:
            block.blitme()


    def set_direction(self, key):
        x_dir = self.directions[key][0]
        y_dir = self.directions[key][1]
        if self.coast_is_clear(x_dir, y_dir):
            self.x_dir = self.directions[key][0]
            self.y_dir = self.directions[key][1]
            self.reset_movement()
            self.movement[key] = True


    def coast_is_clear(self, x_dir, y_dir):
        """Returns true if head is not trying to move into tail."""
        x = self.head_rect.x + self.scale * x_dir
        y = self.head_rect.y + self.scale * y_dir
        if len(self.tail) > 0:
            if self.tail[-1].rect.x == x and self.tail[-1].rect.y == y:
                return False
            return True
        else:
            return True


    def reset_movement(self):
        """Reset movement flags to False."""
        self.movement = {'up': False, 'down': False, 'left': False, 'right': False}


    def intersects(self, x, y, head):
        """
        Checks if x and y intersects with tail. If head == True
        then check if head intersects as well.
        """
        if head:
            if x == self.head_rect.x and y == self.head_rect.y:
                print("intersects with head")
                return True
        else:
            for block in self.tail:
                if x == block.rect.x and y == block.rect.y:
                    print("intersects with tail")
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
