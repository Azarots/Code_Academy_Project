import random
from screen_constants import *


class Food:
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
