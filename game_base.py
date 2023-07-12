import pygame
import methods
from pygame.locals import *

# Pencere boyutları
WIDTH = methods.WIDTH
HEIGHT = methods.HEIGHT

# Oyun tahtası boyutları
BOARD_SIZE = methods.BOARD_SIZE
CELL_SIZE = methods.CELL_SIZE

# Renkler
WHITE = methods.WHITE
BLACK = methods.BLACK
RED = methods.RED
GRAY = methods.GRAY
BLUE = methods.BLUE

# Kazanan belirleme
kazanan_x = methods.kazanan_x
kazanan_o = methods.kazanan_o
sayac = methods.sayac

def draw_board(screen):
    screen.fill(WHITE)
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)
        pygame.draw.line(screen, BLACK, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), 2)


def draw_mark(screen, row, col, mark):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 3
    if mark == 'X':
        pygame.draw.line(screen, RED, (x - radius, y - radius), (x + radius, y + radius), 2)
        pygame.draw.line(screen, RED, (x - radius, y + radius), (x + radius, y - radius), 2)
    elif mark == 'O':
        pygame.draw.circle(screen, BLUE, (x, y), radius, 2)


def get_cell(row, col):
    return col // CELL_SIZE, row // CELL_SIZE


def reset_board():
    return [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]



