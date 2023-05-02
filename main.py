import pygame
import block_
import global_
import snake_
import fonts_
import records_
from random import randrange


def draw_block_by_x_y(x, y, color, indent) -> None:
    pygame.draw.rect(global_.screen, pygame.Color(color), (x + indent,
                     y + indent, global_.SIZE - indent * 2, global_.SIZE - indent * 2))


def draw_block(block, color, indent) -> None:
    draw_block_by_x_y(block.x, block.y, color, indent)


def get_random_empty_block(snake) -> block_.Block:
    while True:
        ans = block_.Block(randrange(0, global_.WINDOW_SIZE, global_.SIZE),
                           randrange(0, global_.WINDOW_SIZE, global_.SIZE))
        if ans not in snake.body:
            return ans


def check_and_end_of_game(snake: snake_.Snake) -> None:
    is_end = (snake.head.x < 0 or snake.head.x > global_.WINDOW_SIZE - global_.SIZE
              or snake.head.y < 0 or snake.head.y > global_.WINDOW_SIZE - global_.SIZE or len(snake.body) != len(set(snake.body)))
    if is_end:
        records_.new_record(snake.name, snake.score)
        fonts_.draw_end()
        pygame.display.flip()
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    cl = event.unicode.lower()
                    if event.key == pygame.K_r or cl == 'r' or cl == 'к':
                        gameloop(snake.name)
                    elif event.key == pygame.K_t or cl == 't' or cl == 'е':
                        records_.draw_records()
                        pygame.display.flip()

cl = 'temp'
key = 'temp'         
def check_events(snake: snake_.Snake) -> None:
    global cl
    global key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            cl = event.unicode.lower()
            key = event.key
            if (cl == 'w' or cl == 'ц' or key == pygame.K_w or key == pygame.K_UP) and snake.d_row == 0:
                snake.buf_d_col, snake.buf_d_row = 0, -1
            elif (cl == 'a' or cl == 'ф' or key == pygame.K_a or key == pygame.K_LEFT) and snake.d_col == 0:
                snake.buf_d_col, snake.buf_d_row = -1, 0
            elif (cl == 's' or cl == 'ы' or key == pygame.K_s or key == pygame.K_DOWN) and snake.d_row == 0:
                snake.buf_d_col, snake.buf_d_row = 0, 1
            elif (cl == 'd' or cl == 'в' or key == pygame.K_d or key == pygame.K_RIGHT) and snake.d_col == 0:
                snake.buf_d_col, snake.buf_d_row = 1, 0
            elif (cl == 'д' or cl == 'l' or key == pygame.K_l):
                snake.pos_color += 1
                snake.pos_color %= len(snake_.Snake.COLORS)
                snake.color = snake_.Snake.COLORS[snake.pos_color]
    if cl != 'temp':
        if (cl == 'w' or cl == 'ц' or key == pygame.K_w or key == pygame.K_UP) and snake.d_row == 0:
            snake.buf_d_col, snake.buf_d_row = 0, -1
        elif (cl == 'a' or cl == 'ф' or key == pygame.K_a or key == pygame.K_LEFT) and snake.d_col == 0:
            snake.buf_d_col, snake.buf_d_row = -1, 0
        elif (cl == 's' or cl == 'ы' or key == pygame.K_s or key == pygame.K_DOWN) and snake.d_row == 0:
            snake.buf_d_col, snake.buf_d_row = 0, 1
        elif (cl == 'd' or cl == 'в' or key == pygame.K_d or key == pygame.K_RIGHT) and snake.d_col == 0:
            snake.buf_d_col, snake.buf_d_row = 1, 0

def scan_key_pressed(snake: snake_.Snake) -> None:
    check_events(snake)
    #key = pygame.key.get_pressed()
    #if (key[pygame.K_UP] or key[pygame.K_w]) and snake.d_row == 0:
    #    snake.buf_d_col, snake.buf_d_row = 0, -1
    #elif (key[pygame.K_LEFT] or key[pygame.K_a]) and snake.d_col == 0:
    #    snake.buf_d_col, snake.buf_d_row = -1, 0
    #elif (key[pygame.K_DOWN] or key[pygame.K_s]) and snake.d_row == 0:
    #    snake.buf_d_col, snake.buf_d_row = 0, 1
    #elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and snake.d_col == 0:
    #    snake.buf_d_col, snake.buf_d_row = 1, 0

def gameloop(name) -> None:
    global cl, key
    cl = key = 'temp'
    running = True
    snake = snake_.Snake()
    snake.name = name
    apple = get_random_empty_block(snake)

    global_.img = pygame.image.load(
        global_.full_path/global_.images[randrange(0, 2)]).convert()
        
    while running:
        global_.screen.blit(global_.img, (0, 0))
        # global_.screen.fill(pygame.Color('black'))

        # drawing snake
        for block in snake.body:
            draw_block(block, snake.color, 1)

        # drawing apple
        draw_block(apple, 'red', 0)

        # show score
        fonts_.draw_score(snake.score)

        # snake movement
        snake.move()

        # eating apple
        if snake.head == apple:
            apple = get_random_empty_block(snake)
            snake.length += 1
            snake.score += 1
            snake.speed += snake.d_speed
            snake.speed = max(snake.speed, snake_.Snake.MIN_SPEED)
            snake.d_speed -= 15
            snake.speed = min(snake.speed, snake_.Snake.MAX_SPEED)

        # game over
        check_and_end_of_game(snake)

        # update global_.screen
        pygame.display.flip()
        global_.clock.tick(global_.FPS)

        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #exit()

        # control
        scan_key_pressed(snake)


name = input("Enter your nick: ")
global_.start()
gameloop(name)
