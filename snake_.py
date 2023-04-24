import block_
import global_
from random import randrange


class Snake:
    def __init__(self) -> None:
        self.length = 1
        self.head = block_.Block(randrange(0, global_.WINDOW_SIZE, global_.SIZE),
                                 randrange(0, global_.WINDOW_SIZE, global_.SIZE))
        self.body = [self.head]
        self.d_row, self.d_col = 0, 0
        self.buf_d_row, self.buf_d_col = 0, 0
        self.score = 0
        self.speed = 6000
        self.time_to_speed = 0
        self.d_speed = 400

        self.UPDATE = 30000
        self.MAXSPEED = self.UPDATE

    def move(self) -> None:
        self.time_to_speed += 1
        if self.time_to_speed * self.speed >= self.UPDATE:
            self.d_col = self.buf_d_col
            self.d_row = self.buf_d_row
            self.time_to_speed = 0
            self.head.x += self.d_row * global_.SIZE
            self.head.y += self.d_col * global_.SIZE
            self.body.append(block_.Block(self.head.x, self.head.y))
            self.body = self.body[-self.length:]
