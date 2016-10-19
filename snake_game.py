import pygame
import ctypes
import game_functions as func
from game_settings import Settings
from snake import Snake

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

        self.clock = pygame.time.Clock()


    def run_game(self):
        """Main function for Snake."""
        while True:
            func.check_events(self.snake)
            func.update_screen(self.screen, self.settings, self.snake)

            self.clock.tick(self.settings.fps)


if __name__ == '__main__':
    Game().run_game()
