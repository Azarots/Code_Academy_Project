import sys
from main import Main
from screen_constants import *

# SCREEN SETTINGS
pygame.init()

# Main
main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = pygame.math.Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = pygame.math.Vector2(0, 1)
            elif event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = pygame.math.Vector2(-1, 0)
            elif event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = pygame.math.Vector2(1, 0)

    screen.fill(("darkgreen"))
    main_game.draw_elements()
    pygame.display.update()

    clock = pygame.time.Clock()
    clock.tick(60)  # FPS
