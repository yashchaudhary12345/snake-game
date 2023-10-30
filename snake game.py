import pygame
import time
import random


pygame.init()


WIDTH, HEIGHT = 640, 480
SNAKE_SIZE = 20
SNAKE_SPEED = 15


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")


snake_x = WIDTH // 2
snake_y = HEIGHT // 2


snake_x_change = 0
snake_y_change = 0


snake_length = 1
snake_list = []


food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)


score = 0


game_over = False


font = pygame.font.Font(None, 36)

def show_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = SNAKE_SIZE
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -SNAKE_SIZE
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = SNAKE_SIZE
                snake_x_change = 0

   
    snake_x += snake_x_change
    snake_y += snake_y_change

    
    if (
        snake_x >= WIDTH
        or snake_x < 0
        or snake_y >= HEIGHT
        or snake_y < 0
    ):
        game_over = True

   
    if (
        snake_x == food_x
        and snake_y == food_y
    ):
        score += 1
        food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
        food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
        snake_length += 1

   
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    
    window.fill((0, 0, 0))
    for segment in snake_list:
        pygame.draw.rect(window, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])
    pygame.draw.rect(window, RED, [food_x, food_y, SNAKE_SIZE, SNAKE_SIZE])

    show_score(score)
    pygame.display.update()

    time.sleep(1 / SNAKE_SPEED)


pygame.quit()
