import pygame
WINDOW_SIZE = 800
SIZE = 50
FPS = 40

pygame.init()
screen = pygame.display.set_mode([WINDOW_SIZE, WINDOW_SIZE])
pygame.display.set_caption("SnakeGame by @FflashkingF")
clock = pygame.time.Clock()