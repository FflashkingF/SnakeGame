import pygame
import pathlib

full_path = pathlib.Path(__file__).parent.resolve()

WINDOW_SIZE = 800
SIZE = 50
FPS = 40
INITIAL_POSITION_FOR_RECORDS = 250

pygame.init()
screen = "temp"
pygame.display.set_caption("SnakeGame by @FflashkingF")
clock = pygame.time.Clock()

images = ['16.jpg', '17.jpg']
img = "temp"
hall = "temp"


def start():
    global screen
    global hall
    screen = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
    hall = pygame.image.load(full_path/'image'/'21.png').convert()
