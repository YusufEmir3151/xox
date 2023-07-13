import pygame
import methods


GREEN = methods.GREEN
WIN_LINE_WIDTH = methods.WIN_LINE_WIDTH
WIN_LINE_ANIMATION_SPEED = methods.WIN_LINE_ANIMATION_SPEED
WIN_LINE_COLOR = methods.WIN_LINE_COLOR

CELL_SIZE = methods.CELL_SIZE
RED = methods.RED
ANIMATION_SPEED = methods.ANIMATION_SPEED
BLUE = methods.BLUE

def animate_mark(screen, row, col, mark):
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = row * CELL_SIZE + CELL_SIZE // 2
    radius = CELL_SIZE // 3

    if mark == 'X':
        for i in range(radius + 1):
            pygame.draw.line(screen, RED, (x - i, y - i), (x + i, y + i), 2)
            pygame.draw.line(screen, RED, (x - i, y + i), (x + i, y - i), 2)
            pygame.time.wait(ANIMATION_SPEED)
            pygame.display.flip()
    elif mark == 'O':
        for i in range(radius + 1):
            pygame.draw.circle(screen, BLUE, (x, y), i, 2)
            pygame.time.wait(ANIMATION_SPEED)
            pygame.display.flip()

def draw_win_line(screen, start_pos, end_pos):
    start_x, start_y = start_pos
    end_x, end_y = end_pos
    delta_x = end_x - start_x
    delta_y = end_y - start_y
    line_length = int(CELL_SIZE * 0.3)  # Çizgi uzunluğunu belirle (karoların 1.5 katı)

    start_x -= int(delta_x * (line_length / (2 * CELL_SIZE)))
    start_y -= int(delta_y * (line_length / (2 * CELL_SIZE)))
    end_x += int(delta_x * (line_length / (2 * CELL_SIZE)))
    end_y += int(delta_y * (line_length / (2 * CELL_SIZE)))

    for i in range(1, 6):
        alpha = 255 - (i * 100)  # Kenarların şeffaflık değeri
        color = (*methods.WIN_LINE_COLOR, alpha)  # Çizgi rengi ve alfa değeri (yeşil)
        width = methods.WIN_LINE_WIDTH - i  # Çizgi kalınlığı
        pygame.draw.line(screen, GREEN, (start_x, start_y), (end_x, end_y), width)
        pygame.time.wait(methods.WIN_LINE_ANIMATION_SPEED)
        pygame.display.flip()






