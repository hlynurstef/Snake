import pygame
from block import Block

def update_screen(screen, snake):
    """Update everything on screen and then draw the screen."""
    screen.fill((0, 0, 0))

    for block in snake:
        block.blitme()

    pygame.display.update()


def check_events():
    """Check for events and respond to them."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_pygame()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def check_keydown_events(event):
    """Check for keypresses and respond to them."""
    if event.key == pygame.K_ESCAPE:
        quit_pygame()


def quit_pygame():
    """Quits pygame and python"""
    pygame.quit()
    quit()

def initialize_snake(screen, settings):
    """Initialize snake object and return it."""
    snake = []
    snake.append(Block(screen, settings, settings.white, 400, 300))
    return snake
