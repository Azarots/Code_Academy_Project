import pygame, sys, random


# SNAKE SETTINGS
class Snake:
    def __init__(self):
        self.body = [pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]
        self.direction = pygame.math.Vector2(0, 0)  # Start Direction
        self.new_block = False

        # Snake Body images
        self.head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("Graphics/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("Graphics/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("Graphics/tail_left.png").convert_alpha()

        self.body_vertical = pygame.image.load("Graphics/body_vertical.png").convert_alpha()
        self.body_horizontal = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()

        self.body_tr = pygame.image.load("Graphics/body_topright.png").convert_alpha()
        self.body_tl = pygame.image.load("Graphics/body_topleft.png").convert_alpha()
        self.body_br = pygame.image.load("Graphics/body_bottomright.png").convert_alpha()
        self.body_bl = pygame.image.load("Graphics/body_bottomleft.png").convert_alpha()

        # Sound Effects
        self.food_sound = pygame.mixer.Sound("Sound/eating-sound-effect-36186.mp3")
        self.game_over_sound = pygame.mixer.Sound("Sound/videogame-death-sound-43894.mp3")
        # back_ground_sound = pygame.mixer.Sound("Sound/Back_Ground.mp3")
        # back_ground_sound.play(-1)
        pygame.mixer.pre_init(44100, -16, 2, 512)  # Avoids delay on a sound.

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)  # head
            elif index == len(self.body) - 1:  # By this method we will get last item.
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)  # x = -1, y = -1
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)  # x = -1, y = 1
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)  # x = 1, y = -1
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)  # x = 1, y = 1

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == pygame.math.Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == pygame.math.Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == pygame.math.Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == pygame.math.Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == pygame.math.Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == pygame.math.Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == pygame.math.Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == pygame.math.Vector2(0, -1):
            self.tail = self.tail_down

            # TESTING
            # x_pos = int(block.x * cell_size)
            # y_pos = int(block.y * cell_size)
            # block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)  # pygame.Rect(x, y, width, height)
            # pygame.draw.rect(screen, "forestgreen", block_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False  # Changing condition from TRUE to FALSE, so our snake won't have infinitive tail.
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_eating_sound(self):
        self.food_sound.play()

    def reset_snake(self):
        self.body = [pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]
        self.direction = pygame.math.Vector2(0, 0)


# FRUIT/FOOD SETTINGS
class Fruit:
    def __init__(self):
        self.randomize()  # Trying to save some code lines, that's why added randomize because used same logic.
        self.food = pygame.image.load("Graphics/apple.png").convert_alpha()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.food, fruit_rect)
        # pygame.draw.rect(screen, "brown1", fruit_rect)  # Surface, color, rectagle

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)  # Ensures that fruit is alawys on the screen
        self.y = random.randint(0, cell_number - 1)
        self.pos = pygame.math.Vector2(self.x, self.y)  # Can Import pygame.math to save some writitng time.


# MAIN CALL
class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def draw_score(self):
        score_text = str(len(self.snake.body) - 2)
        score_surface = game_font.render(score_text, False, "bisque4")
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        food_rect = self.fruit.food.get_rect(midright=(score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.food, food_rect)  # Change Icon in the future!.

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
        # Should add game over sound.
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[
            0].y < cell_number:  # Checking if snake is outisde of the screen (RIGHT LEFT 'X', TOP, BOTTOM 'Y').
            self.game_over()
        # I should add sound when snake eat a tail.
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                # Vieta kur yra bug.
                self.game_over()

    def game_over(self):
        self.snake.reset_snake()
        self.snake.game_over_sound.play()


# SCREEN SETTINGS
pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

# Game Images/SOUND
# food = pygame.image.load("Graphics/apple.png").convert_alpha()  # Python image converter


# SCORE
game_font = pygame.font.Font("Font/game_over.ttf", 100)  # Font and font Size

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
    clock.tick(60)  # FPS

# Add a leaderboard to your game, where players can view the high scores of all time or for the day/week/month.
# Implement sound effects and music to enhance the gaming experience. (Left the Game Over, Bite Tail, and Wall Sound).
# Implement unit tests and code reviews to ensure that your code is high quality and free of bugs.
# Create an EXE file.
# Add RESET and MUTE Buttons.

# Class Small start (DONE)
# BlackFormater/ Black Python / Line lenght 120. black .
# Classes istaukt i kitus failus.
# Add option to mute the sound.
# Add to the GITHUB