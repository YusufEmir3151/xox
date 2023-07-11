import pygame
from pygame.locals import *

# Pencere boyutları
WIDTH = 300
HEIGHT = 300

# Oyun tahtası boyutları
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_board(screen):
    screen.fill(WHITE)
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)
        pygame.draw.line(screen, BLACK, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), 2)

def draw_mark(screen, row, col, mark):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 3
    pygame.draw.circle(screen, BLACK, (x, y), radius, 2)
    if mark == 'X':
        pygame.draw.line(screen, BLACK, (x - radius, y - radius), (x + radius, y + radius), 2)
        pygame.draw.line(screen, BLACK, (x - radius, y + radius), (x + radius, y - radius), 2)
    elif mark == 'O':
        pygame.draw.circle(screen, BLACK, (x, y), radius // 2, 2)

def get_cell(row, col):
    return col // CELL_SIZE, row // CELL_SIZE

def reset_board():
    return [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("XOX Oyunu")

    board = reset_board()
    turn = 'X'
    game_over = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if game_over:
                    board = reset_board()
                    turn = 'X'
                    game_over = False
                else:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    col, row = get_cell(mouseY, mouseX)
                    if board[row][col] == '':
                        board[row][col] = turn
                        draw_mark(screen, row, col, turn)
                        turn = 'O' if turn == 'X' else 'X'

        draw_board(screen)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] != '':
                    draw_mark(screen, row, col, board[row][col])

        if not game_over:
            # Oyun kontrolü
            for i in range(BOARD_SIZE):
                if board[i][0] == board[i][1] == board[i][2] != '':
                    pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2),
                                     (WIDTH - CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), 3)
                    game_over = True
                if board[0][i] == board[1][i] == board[2][i] != '':
                    pygame.draw.line(screen, BLACK, (i * CELL_SIZE + CELL_SIZE // 2, CELL_SIZE // 2),
                                     (i * CELL_SIZE + CELL_SIZE // 2, HEIGHT - CELL_SIZE // 2), 3)
                    game_over = True
            if board[0][0] == board[1][1] == board[2][2] != '':
                pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, CELL_SIZE // 2),
                                 (WIDTH - CELL_SIZE // 2, HEIGHT - CELL_SIZE // 2), 3)
                game_over = True
            if board[0][2] == board[1][1] == board[2][0] != '':
                pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, HEIGHT - CELL_SIZE // 2),
                                 (WIDTH - CELL_SIZE // 2, CELL_SIZE // 2), 3)
                game_over = True

        if game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("Oyun Bitti!", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            text = font.render("Yeniden Oynamak için Tıklayın", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + text.get_height()))

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()