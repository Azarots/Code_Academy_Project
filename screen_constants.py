import pygame
from logger_config import logger

cell_size = 30  # Worked with the 40 (Home screen).
cell_number = 20

try:
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
except pygame.error as screen_error:
    logger.error(f"Failed to create screen surface: {screen_error}")
