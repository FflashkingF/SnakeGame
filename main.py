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


class Head:
    head = Block(randrange(0, WINDOW_SIZE, SIZE),
                 randrange(0, WINDOW_SIZE, SIZE))


class Apple:
    apple = Block(randrange(0, WINDOW_SIZE, SIZE),
                  randrange(0, WINDOW_SIZE, SIZE))


class Snake:
    lenght = 1
    body = [Head.head]
    d_row, d_col = 0, 0
    buf_d_row, buf_d_col = 0, 0
    score = 0
    speed = 6000
    time_to_speed = 0
    d_speed = 400

    UPDATE = 30000
    MAXSPEED = UPDATE


pygame.init()
screen = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
fps = 40


def draw_block_by_x_y(x, y, color, indent) -> None:
    pygame.draw.rect(screen, pygame.Color(color), (x + indent,
                     y + indent, SIZE - indent, SIZE - indent))


def draw_block(block, color, indent) -> None:
    draw_block_by_x_y(block.x, block.y, color, indent)


def get_random_empty_block() -> Block:
    while True:
        ans = Block(randrange(0, WINDOW_SIZE, SIZE),
                    randrange(0, WINDOW_SIZE, SIZE))
        if ans not in Snake.body:
          return ans


while True:
    screen.fill(pygame.Color('black'))

    # drawing snake
    for block in Snake.body:
        draw_block(block, 'green', 1)

    # drawing apple
    draw_block(Apple.apple, 'red', 0)

    # show score
    render_score = font_score.render(
        f'SCORE: {Snake.score}', 1, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))

    # snake movement
    Snake.time_to_speed += 1
    if Snake.time_to_speed * Snake.speed >= Snake.UPDATE:
        Snake.d_col = Snake.buf_d_col
        Snake.d_row = Snake.buf_d_row
        Snake.time_to_speed = 0
        Head.head.x += Snake.d_row * SIZE
        Head.head.y += Snake.d_col * SIZE
        Snake.body.append(Block(Head.head.x, Head.head.y))
        Snake.body = Snake.body[-Snake.lenght:]

    # eating Apple
    if Head.head == Apple.apple:
        Apple.apple = get_random_empty_block()
        Snake.lenght += 1
        Snake.score += 1
        Snake.speed += Snake.d_speed
        Snake.d_speed -= 15
        Snake.speed = min(Snake.speed, Snake.MAXSPEED)

    # game over
    is_end = (Head.head.x < 0 or Head.head.x > WINDOW_SIZE - SIZE
              or Head.head.y < 0 or Head.head.y > WINDOW_SIZE - SIZE or len(Snake.body) != len(set(Snake.body)))
    if is_end:
        while True:
            render_end = font_end.render(
                'GAME OVER', 1, pygame.Color('orange'))
            screen.blit(render_end, (WINDOW_SIZE // 2 - 200, WINDOW_SIZE // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
    
    #update screen
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # control
    key = pygame.key.get_pressed()
    if (key[pygame.K_UP] or key[pygame.K_w]) and Snake.d_col == 0:
        Snake.buf_d_row, Snake.buf_d_col = 0, -1
    elif (key[pygame.K_LEFT] or key[pygame.K_a]) and Snake.d_row == 0:
        Snake.buf_d_row, Snake.buf_d_col = -1, 0
    elif (key[pygame.K_DOWN] or key[pygame.K_s]) and Snake.d_col == 0:
        Snake.buf_d_row, Snake.buf_d_col = 0, 1
    elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and Snake.d_row == 0:
        Snake.buf_d_row, Snake.buf_d_col = 1, 0
