import pygame
from random import randrange

WINDOW_SIZE = 800
SIZE = 50


class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return self.x + self.y * WINDOW_SIZE

    def is_inside(self) -> bool:
        return 0 <= self.x < WINDOW_SIZE - SIZE and 0 <= self.y < WINDOW_SIZE - SIZE

    def __eq__(self, other) -> bool:
        return isinstance(other, Block) and self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return f'Block({self.x}, {self.y})'

    def __repr__(self) -> str:
        return self.__str__()


class Apple:
    apple = Block(randrange(0, WINDOW_SIZE, SIZE),
                  randrange(0, WINDOW_SIZE, SIZE))


class Snake:
    
    def __init__(self) -> None:
        self.length = 1
        self.head = Block(randrange(0, WINDOW_SIZE, SIZE),
                    randrange(0, WINDOW_SIZE, SIZE))
        self.body = [self.head]
        self.d_row, self.d_col = 0, 0
        self.buf_d_row, self.buf_d_col = 0, 0
        self.score = 0
        self.speed = 6000
        self.time_to_speed = 0
        self.d_speed = 400

        self.UPDATE = 30000
        self.MAXSPEED = self.UPDATE


pygame.init()
screen = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
pygame.display.set_caption("SnakeGame by @FflashkingF")
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
FPS = 40


def draw_block_by_x_y(x, y, color, indent) -> None:
    pygame.draw.rect(screen, pygame.Color(color), (x + indent,
                     y + indent, SIZE - indent * 2, SIZE - indent * 2))


def draw_block(block, color, indent) -> None:
    draw_block_by_x_y(block.x, block.y, color, indent)


def get_random_empty_block(snake) -> Block:
    while True:
        ans = Block(randrange(0, WINDOW_SIZE, SIZE),
                    randrange(0, WINDOW_SIZE, SIZE))
        if ans not in snake.body:
            return ans


def gameloop() -> None:
    running = True
    snake = Snake()
    apple = Apple()
    while running:
        screen.fill(pygame.Color('black'))
        # drawing snake
        for block in snake.body:
            draw_block(block, 'green', 1)

        # drawing apple
        draw_block(apple.apple, 'red', 0)

        # show score
        render_score = font_score.render(
            f'SCORE: {snake.score}', 1, pygame.Color('orange'))
        screen.blit(render_score, (5, 5))

        # snake movement
        snake.time_to_speed += 1
        if snake.time_to_speed * snake.speed >= snake.UPDATE:
            snake.d_col = snake.buf_d_col
            snake.d_row = snake.buf_d_row
            snake.time_to_speed = 0
            snake.head.x += snake.d_row * SIZE
            snake.head.y += snake.d_col * SIZE
            snake.body.append(Block(snake.head.x, snake.head.y))
            snake.body = snake.body[-snake.length:]

        # eating apple
        if snake.head == apple.apple:
            apple.apple = get_random_empty_block(snake)
            snake.length += 1
            snake.score += 1
            snake.speed += snake.d_speed
            snake.d_speed -= 15
            snake.speed = min(snake.speed, snake.MAXSPEED)

        # game over
        is_end = (snake.head.x < 0 or snake.head.x > WINDOW_SIZE - SIZE
                  or snake.head.y < 0 or snake.head.y > WINDOW_SIZE - SIZE or len(snake.body) != len(set(snake.body)))
        if is_end:
            running = False
            while True:
                render_end = font_end.render(
                    'GAME OVER', 1, pygame.Color('orange'))
                screen.blit(render_end, (WINDOW_SIZE //
                            2 - 200, WINDOW_SIZE // 3))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            gameloop()

        # update screen
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # control
        key = pygame.key.get_pressed()
        if (key[pygame.K_UP] or key[pygame.K_w]) and snake.d_col == 0:
            snake.buf_d_row, snake.buf_d_col = 0, -1
        elif (key[pygame.K_LEFT] or key[pygame.K_a]) and snake.d_row == 0:
            snake.buf_d_row, snake.buf_d_col = -1, 0
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and snake.d_col == 0:
            snake.buf_d_row, snake.buf_d_col = 0, 1
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and snake.d_row == 0:
            snake.buf_d_row, snake.buf_d_col = 1, 0


gameloop()
