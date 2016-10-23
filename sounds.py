import pygame

class Sounds():
    """A class to store all sounds in Snake."""

    def __init__(self):
        """Initialize Sound."""
        self.eat_food = pygame.mixer.Sound("sounds/eat_food.wav")
        self.hurt     = pygame.mixer.Sound("sounds/hurt.wav")
        self.music    = pygame.mixer.Sound("sounds/arcade_music_loop.wav")
        self.eat_food.set_volume(.5)
        self.music.set_volume(.75)
