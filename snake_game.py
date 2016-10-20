import pygame
import ctypes
import game_functions as func
from game_settings import Settings
from snake import Snake
from block import Block

class Game():
    """A class representing the game."""

    def __init__(self):
        """Initialize game."""
        pygame.init()

        # Ensure correct screen size to be displayed.
        ctypes.windll.user32.SetProcessDPIAware()
        # Set screensize and caption.
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption(self.settings.caption)

        self.snake = Snake(self.screen, self.settings)
        self.food = func.create_food(self.screen, self.settings, self.snake)
        self.keys = {'up': False, 'down': False, 'left': False, 'right': False}

        self.clock = pygame.time.Clock()


    def run_game(self):
        """Main function for Snake."""
        while True:
            func.check_events(self.keys, self.snake)
            func.check_edges(self.settings, self.snake)
            func.check_hit_tail(self.snake)
            func.update_screen(self.screen, self.settings, self.snake, self.food)

            self.clock.tick(self.settings.fps)


if __name__ == '__main__':
    Game().run_game()
