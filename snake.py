from screen_constants import *


class Snake:
    def __init__(self):
        self.body = [pygame.math.Vector2(4, 10), pygame.math.Vector2(3, 10)]  # 2 Bodies (Head and Tail) + Start pos.
        self.direction = pygame.math.Vector2(0, 0)  # Start Direction
        self.new_block = False  # if collision with the food changes to true.

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
        back_ground_sound = pygame.mixer.Sound("Sound/Back_Ground.mp3")
        # back_ground_sound.set_volume(0)
        back_ground_sound.play(-1)  # Sound Playing on repeat.
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
            elif index == len(self.body) - 1:  # By this method we will get last item (Tail).
                screen.blit(self.tail, block_rect)
            else:  # Horizontal and Vertical body.
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:  # Corners of the body (Looking into current and previous block, and how they correlate together)
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

    def move_snake(self):
        if self.new_block == True:  # When changes to true add new block.
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False  # Changing condition from TRUE to FALSE, so our snake won't have infinitive tail.
        else:
            if self.direction != pygame.math.Vector2(0, 0):  # Fixed issue with the overlapping spend 6 hours....
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
