import pygame
from block import Block
from random import randint

def update_screen(screen, settings, sounds, snake, food):
    """Update everything on screen and then draw the screen."""
    screen.fill(settings.black)
    ate = snake_ate_food(sounds, snake, food)
    if ate:
        create_food(screen, settings, snake, food)
    food.blitme()
    #print("(" + str(food.rect.x) + ", " + str(food.rect.y) + ")")

    snake.update(ate)
    snake.blitme()

    pygame.display.update()


def check_events(keys, snake):
    """Check for events and respond to them."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_pygame()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, keys, snake)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, keys)
        move_snake(keys, snake)


def check_keydown_events(event, keys, snake):
    """Check for keypresses and respond to them."""
    if event.key == pygame.K_ESCAPE:
        quit_pygame()
    if event.key == pygame.K_UP:
        keys['up'] = True
    if event.key == pygame.K_DOWN:
        keys['down'] = True
    if event.key == pygame.K_LEFT:
        keys['left'] = True
    if event.key == pygame.K_RIGHT:
        keys['right'] = True


def check_keyup_events(event, keys):
    """Check for keyreleases and respond to them."""
    if event.key == pygame.K_UP:
        keys['up'] = False
    if event.key == pygame.K_DOWN:
        keys['down'] = False
    if event.key == pygame.K_LEFT:
        keys['left'] = False
    if event.key == pygame.K_RIGHT:
        keys['right'] = False


def move_snake(keys, snake):
    """Move snake if only one key is being pressed."""
    count = 0
    key_pressed = ''
    for key, pressed in keys.items():
        if pressed:
            key_pressed = key
            count += 1
    if count == 1:
        snake.set_direction(key_pressed)


def quit_pygame():
    """Quits pygame and python."""
    pygame.quit()
    quit()


def check_edges(settings, sounds, snake):
    """Check if snake is beyond the edges."""
    if ((snake.head_rect.x + settings.scale > settings.width) or
       (snake.head_rect.x < 0) or
       (snake.head_rect.y + settings.scale > settings.height) or
       (snake.head_rect.y < 0)):
       sounds.hurt.play()
       snake.initialize_snake()


def check_hit_tail(sounds, snake):
    """Check if snake hits its own tail."""
    if snake.intersects(snake.head_rect.x, snake.head_rect.y, False):
        sounds.hurt.play()
        snake.initialize_snake()


def create_food(screen, settings, snake, food=None):
    """Creates a food at a random location."""
    intersects = True
    while True:
        x = randint(0, settings.width)
        x = x - (x % settings.scale)
        y = randint(0, settings.height)
        y = y - (y % settings.scale)
        if not snake.intersects(x, y, True):
            break
    if food is None:
        food = Block(screen, settings, settings.red, x, y)
        return food
    else:
        food.rect.x = x
        food.rect.y = y


def snake_ate_food(sounds, snake, food):
    """Returns true if the snake has eaten the food."""
    if (snake.head_rect.x == food.rect.x and
        snake.head_rect.y == food.rect.y):
        sounds.eat_food.play()
        return True
    else:
        return False
