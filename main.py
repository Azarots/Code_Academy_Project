import time
from snake import Snake
from food import Food
from screen_constants import *


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Food()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def draw_score(self):
        # SCORE
        game_font = pygame.font.Font("Font/game_over.ttf", 50)  # Font and font Size
        score_value = str(len(self.snake.body) - 2)
        score_text = "SCORE: " + score_value
        score_surface = game_font.render(score_text, True, (255, 255, 255))
        score_x = int(cell_size * cell_number // 2)
        score_y = 20
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:  # If firs body part at the fruit pos makes collision effect.
            self.fruit.randomize()  # Reposition fruit
            self.snake.add_block()  # Add another block to snake
            self.snake.play_eating_sound()  # Playing sound when snake has collision.

        # Avoiding food to be placed on a SNAKE:
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number
        ):  # Checking if snake is outside the screen (RIGHT LEFT 'X', TOP, BOTTOM 'Y').
            self.game_over()
        if len(self.snake.body) > 2:
            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

    def game_over(self):
        self.snake.game_over_sound.play()

        score_font = pygame.font.Font("Font/game_over.ttf", 80)
        score_text = score_font.render(f"SCORE: {len(self.snake.body) - 2}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(cell_number * cell_size / 2, cell_number * cell_size / 2))

        game_over_font = pygame.font.Font("Font/game_over.ttf", 120)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
        game_over_rect = game_over_text.get_rect(center=(cell_number * cell_size / 2, cell_number * cell_size / 4))

        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)

        pygame.display.update()

        time.sleep(1)
        self.snake.reset_snake()
