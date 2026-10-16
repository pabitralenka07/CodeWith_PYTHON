import pygame
import random
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Snake Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (169, 169, 169)
GOLD = (255, 215, 0)
snake_block = 20
initial_speed = 8
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
def your_score(score, level):
    value = score_font.render(f"Score: {score} | Level: {level}", True, GREEN)
    screen.blit(value, [10, 10])
def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(screen, color, [x[0], x[1], snake_block, snake_block])
def message(msg, color, position):
    msg_surface = font_style.render(msg, True, color)
    screen.blit(msg_surface, position)
def game_over_screen():
    screen.fill(BLUE)
    message("Game Over!", RED, [WIDTH / 3, HEIGHT / 3])
    message("Press R to Restart or Q to Quit", WHITE, [WIDTH / 4.5, HEIGHT / 2])
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    return True
                elif event.key == pygame.K_q: 
                    pygame.quit()
                    quit()
def game_loop():
    game_over = False
    x1, y1 = WIDTH // 2, HEIGHT // 2
    x1_change, y1_change = 0, 0
    snake_list = []
    length_of_snake = 1
    score = 0
    level = 1
    speed = initial_speed
    foodx = round(random.randrange(40, WIDTH - 40 - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(40, HEIGHT - 40 - snake_block) / snake_block) * snake_block
    golden_food = None
    golden_timer = 0
    walls = []
    clock = pygame.time.Clock()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and x1_change == 0: 
                    x1_change = -snake_block
                    y1_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and y1_change == 0: 
                    y1_change = -snake_block
                    x1_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and y1_change == 0: 
                    y1_change = snake_block
                    x1_change = 0
        x1 += x1_change
        y1 += y1_change
        if x1 < 40 or x1 >= WIDTH - 40 or y1 < 40 or y1 >= HEIGHT - 40:
            game_over = True
        for wall in walls:
            if wall[0] <= x1 < wall[0] + wall[2] and wall[1] <= y1 < wall[1] + wall[3]:
                game_over = True
        screen.fill(WHITE)
        pygame.draw.rect(screen, GRAY, [0, 0, WIDTH, 40]) 
        pygame.draw.rect(screen, GRAY, [0, HEIGHT - 40, WIDTH, 40]) 
        pygame.draw.rect(screen, GRAY, [0, 0, 40, HEIGHT]) 
        pygame.draw.rect(screen, GRAY, [WIDTH - 40, 0, 40, HEIGHT])
        pygame.draw.rect(screen, GREEN, [foodx, foody, snake_block, snake_block])
        if golden_food:
            pygame.draw.rect(screen, GOLD, [golden_food[0], golden_food[1], snake_block, snake_block])
        for wall in walls:
            pygame.draw.rect(screen, BLACK, wall)
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True
        our_snake(snake_block, snake_list, BLUE)
        your_score(score, level)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(40, WIDTH - 40 - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(40, HEIGHT - 40 - snake_block) / snake_block) * snake_block
            length_of_snake += 1
            score += 10
        if golden_food and x1 == golden_food[0] and y1 == golden_food[1]:
            golden_food = None
            golden_timer = 0
            score += 50
        if not golden_food and random.randint(1, 100) > 98: 
            golden_food = [
                round(random.randrange(40, WIDTH - 40 - snake_block) / snake_block) * snake_block,
                round(random.randrange(40, HEIGHT - 40 - snake_block) / snake_block) * snake_block
            ]
            golden_timer = 100 
        if golden_food:
            golden_timer -= 1
            if golden_timer <= 0:
                golden_food = None
        if score // (level * 50) >= 1:
            level += 1
            speed += 2
            walls.append([
                round(random.randrange(40, WIDTH - 100) / snake_block) * snake_block,
                round(random.randrange(40, HEIGHT - 100) / snake_block) * snake_block,
                snake_block * 5, 
                snake_block 
            ])
        clock.tick(speed)
    if game_over_screen():
        game_loop()
game_loop()