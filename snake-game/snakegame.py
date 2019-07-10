import pygame, random, time
from pygame.locals import*


def random_apple_pos():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


def collision(snake, apple):
    return (snake[0] == apple[0] and snake[1] == apple[1])

def border_colision(snake):
    if snake[0][0] == 590 or snake[0][0] == 0:
        return True
    elif snake[0][1] == 590 or snake[0][1] == 0:
        return True


# SNAKE MOVES
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

# Snake
snake = [(200, 200), (210, 200), (230, 200)]
snake_body = pygame.Surface((10,10))
snake_body.fill((124,252,0))

# Apple
apple = pygame.Surface((10,10))
apple_pos = random_apple_pos()
apple.fill((255, 0, 0))

direction = LEFT

clock = pygame.time.Clock()
aux = 0
while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    # Get key pressed to move snake
    if event.type == KEYDOWN:
        if event.key == K_UP and direction != DOWN:
            direction = UP
        elif event.key == K_DOWN and direction != UP:
            direction = DOWN
        elif event.key == K_RIGHT and direction != LEFT:
            direction = RIGHT
        elif event.key == K_LEFT and direction != RIGHT:
            direction = LEFT

    # Verify if snake eats apple
    if collision(snake[0], apple_pos):
        apple_pos = random_apple_pos()
        snake.append((0,0))
    if border_colision(snake):
        break

    # Change snake body parts positions
    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])
        if i > 2 and snake[i] == snake [0]:
            aux = 1
    if aux == 1:
        break
    # The fill and some other events of our game screen
    screen.fill((255, 255, 255))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_body, pos)


    pygame.display.update()