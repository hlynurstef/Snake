import pygame
from block import Block
from random import randint

def update_screen(screen, settings, snake, food):
    """Update everything on screen and then draw the screen."""
    screen.fill(settings.black)
    ate = snake_ate_food(snake, food)
    if ate:
        create_food(screen, settings, food)
    food.blitme()

    snake.update(ate)
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
    # TODO: Find a way to prevent player from pressing down + left/right quickly to go backwards.
    if event.key == pygame.K_ESCAPE:
        quit_pygame()
    if event.key == pygame.K_UP and not snake.moving_down:
        snake.set_direction(0, -1)
    elif event.key == pygame.K_DOWN and not snake.moving_up:
        snake.set_direction(0, 1)
    elif event.key == pygame.K_LEFT and not snake.moving_right:
        snake.set_direction(-1, 0)
    elif event.key == pygame.K_RIGHT and not snake.moving_left:
        snake.set_direction(1, 0)


def quit_pygame():
    """Quits pygame and python."""
    pygame.quit()
    quit()


def check_edges(settings, snake):
    """Check if snake is beyond the edges."""
    if ((snake.rect.x + settings.scale > settings.width) or
       (snake.rect.x < 0) or
       (snake.rect.y + settings.scale > settings.height) or
       (snake.rect.y < 0)):
        snake.initialize_snake()


def create_food(screen, settings, food=None):
    """Creates a food at a random location."""
    x = randint(0, settings.width)
    x = x - (x % settings.scale)
    y = randint(0, settings.height)
    y = y - (y % settings.scale)
    if food is None:
        food = Block(screen, settings, settings.red, x, y)
        return food
    else:
        food.rect.x = x
        food.rect.y = y


def snake_ate_food(snake, food):
    """Returns true if the snake has eaten the food."""
    if (snake.head.rect.x == food.rect.x and
        snake.head.rect.y == food.rect.y):
        #snake.add_tail()
        return True
    else:
        return False
