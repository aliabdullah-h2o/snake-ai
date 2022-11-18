from os import environ
from snake import *
import pygame

def draw(game_screen, snake, food):
    x = 0
    y = 0
    for r in range(ROWS):
        x = x + SQUARE_SIZE_X
        y = y + SQUARE_SIZE_Y
        
        pygame.draw.line(game_screen, GRID_COLOR, (x, 0), (x, HEIGHT))
        pygame.draw.line(game_screen, GRID_COLOR, (0, y), (WIDTH, y))
        #pygame.draw.rect --> (x0, y0, x_len, y_len)  = (col0, row0, cols, rows)
        #print(Q_SPACE[0,0])

        pygame.draw.rect(game_screen, (255, 255, 255), Q_SPACE[tuple(food.pos)])
        for body_pos in snake.body_pos:
            if tuple(body_pos) in Q_SPACE.keys():
                pygame.draw.rect(game_screen, (255, 255, 255), Q_SPACE[tuple(body_pos)])
            else:
                return True
    
    return False

if __name__ == "__main__":
    pygame.init()
    environ["SDL_VIDEO_CENTERED"] = "1"
    game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game_clock = pygame.time.Clock()
    exit_game = False
    snake = Snake()
    direction = (0,0)
    start = False
    food = Food(snake)

    while not exit_game:
        game_screen.fill(SCREEN_COLOR)
        exit_game = draw(game_screen, snake, food)
        inc = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game=True
            
            if event.type == pygame.KEYDOWN:
                start= True

                if event.key == pygame.K_w:
                    if direction != (0, 1):
                        direction = (0, -1)
                    
                if event.key == pygame.K_s:
                    if direction != (0, -1):
                        direction = (0, 1)
                    
                if event.key == pygame.K_a:
                    if direction != (1, 0):
                        direction = (-1, 0)
                
                if event.key == pygame.K_d:
                    if direction != (-1, 0):
                        direction = (1, 0)

                # if event.key == pygame.K_c:
                #     snake.eat(food)

        if start:
            snake.check_food_collision(food)
            snake.move(direction)
            if snake.is_alive() == False:
                exit_game = True

        pygame.display.update()
        game_clock.tick(FPS)

    pygame.quit()
    quit()