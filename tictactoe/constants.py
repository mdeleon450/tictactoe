import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH//COLS

RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (128,128,128)

X = pygame.transform.scale(pygame.image.load('assets/pngwing.com (1).png'), (200,200))
O = pygame.transform.scale(pygame.image.load('assets/pngwing.com.png'), (200,200))
