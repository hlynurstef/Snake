import pygame
from block import Block

def update_screen(screen, settings, snake):
    """Update everything on screen and then draw the screen."""
    screen.fill((0, 0, 0))

    snake.update()
    snake.blitme()
    check_edges(settings, snake)

    pygame.display.update()


def check_events(snake):
    """Check for events and respond to them."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_pygame()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


def check_keydown_events(event, snake):
    """Check for keypresses and respond to them."""
    if event.key == pygame.K_ESCAPE:
        quit_pygame()
    if event.key == pygame.K_UP:
        snake.set_direction(0, -1)
    if event.key == pygame.K_DOWN:
        snake.set_direction(0, 1)
    if event.key == pygame.K_LEFT:
        snake.set_direction(-1, 0)
    if event.key == pygame.K_RIGHT:
        snake.set_direction(1, 0)


def quit_pygame():
    """Quits pygame and python"""
    pygame.quit()
    quit()


def check_edges(settings, snake):
    """Check if snake is touching the edges."""
    if ((snake.rect.x + settings.scale >= settings.width) or
       (snake.rect.x <= 0) or
       (snake.rect.y + settings.scale >= settings.height) or
       (snake.rect.y <= 0)):
        snake.initialize_snake()
