import pygame
import pathlib

full_path = pathlib.Path(__file__).parent.resolve()

WINDOW_SIZE = 800
SIZE = 50
FPS = 40

pygame.init()
screen = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
pygame.display.set_caption("SnakeGame by @FflashkingF")
clock = pygame.time.Clock()

images = ['16.jpg', '17.jpg']
img = pygame.image.load(full_path/'17.jpg').convert()
hall = pygame.image.load(full_path/'20.jpg').convert()