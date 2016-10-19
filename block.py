import pygame
from pygame.sprite import Sprite

class Block(Sprite):
    """A class representing the snake."""

    def __init__(self, screen, settings, color, x, y):
        """Initialize the Snake."""
        super(Block, self).__init__()
        self.screen = screen
        self.settings = settings
        self.speed = settings.speed

        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        """Draw the block at its current location."""
        self.screen.blit(self.image, self.rect)
