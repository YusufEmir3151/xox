import pygame
import methods
import game_base
import Settings

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
GREEN =methods.GREEN

# Ayarlar
fullscreen = False  # Tam ekran ayarı
first_player = 'X'  # İlk oyuncu ayarı ('X' veya 'O')
second_player = 'O'  # İkinci oyuncu ayarı ('X' veya 'O')

# Kazanan belirleme
kazanan_x = methods.kazanan_x
kazanan_o = methods.kazanan_o
sayac = methods.sayac

# Tuş ayarları
QUIT = game_base.QUIT
MOUSEBUTTONDOWN = game_base.MOUSEBUTTONDOWN

screen = methods.screen
title_text = methods.title_text
first_player_text = methods.first_player_text

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if methods.fullscreen_checkbox.collidepoint(mouse_pos):
                fullscreen = not fullscreen
                Settings.toggle_fullscreen(screen)
            elif methods.first_player_x_button.collidepoint(mouse_pos):
                first_player = 'X'
            elif methods.first_player_o_button.collidepoint(mouse_pos):
                first_player = 'O'
            elif methods.start_game_button.collidepoint(mouse_pos):
                running = False

    screen.fill(WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 20))
    screen.blit(methods.fullscreen_text, (90, 100))
    screen.blit(first_player_text, (90, 150))
    screen.blit(methods.start_game_text, (WIDTH // 2 - methods.start_game_text.get_width() // 2, HEIGHT - 90))

    pygame.draw.rect(screen, BLACK, methods.fullscreen_checkbox, 2)
    if fullscreen:
        pygame.draw.rect(screen, BLACK, methods.fullscreen_checkbox.inflate(-10, -10))

    pygame.draw.rect(screen, BLACK, methods.first_player_x_button, 2)
    if first_player == 'X':
        pygame.draw.rect(screen, RED, methods.first_player_x_button.inflate(-10, -10))
        first_player_x_text = methods.font.render("X", True, WHITE)
        screen.blit(first_player_x_text, (25, 155))

    pygame.draw.rect(screen, BLACK, methods.first_player_o_button, 2)
    if first_player == 'O':
        pygame.draw.rect(screen, BLUE, methods.first_player_o_button.inflate(-10, -10))
        first_player_o_text = methods.font.render("O", True, WHITE)
        screen.blit(first_player_o_text, (55, 155))

    pygame.display.flip()

pygame.quit()
def main():
    global kazanan_x, kazanan_o, sayac
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("XOX Oyunu")

    board = game_base.reset_board()
    turn = 'X'
    game_over = False
    game_over_draw = False
    winning_cells = []  # Cells for drawing the winning line

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if game_over:
                    board = game_base.reset_board()
                    turn = 'X'
                    game_over = False
                    game_over_draw = False
                    kazanan_o = False
                    kazanan_x = False
                    sayac = 0
                    winning_cells = []
                elif game_over_draw:
                    board = game_base.reset_board()
                    turn = 'X'
                    game_over_draw = False
                    game_over = False
                    winning_cells = []
                else:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    col, row = game_base.get_cell(mouseY, mouseX)
                    if board[row][col] == '':
                        board[row][col] = turn
                        game_base.draw_mark(screen, row, col, turn)
                        turn = 'O' if turn == 'X' else 'X'
        game_base.draw_board(screen)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] != '':
                    game_base.draw_mark(screen, row, col, board[row][col])

        if not game_over:
            # Oyun kontrolü
            for i in range(BOARD_SIZE):
                # yatay yapınca
                if board[i][0] == board[i][1] == board[i][2] != '':
                    pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2),
                                     (WIDTH - CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), 3)
                    winning_cells = [(i, 0), (i, 1), (i, 2)]
                    if turn == 'X':
                        kazanan_o = True
                    if turn == 'O':
                        kazanan_x = True
                    game_over = True
                    sayac = 1
                # dikey yapınca
                if board[0][i] == board[1][i] == board[2][i] != '':
                    pygame.draw.line(screen, BLACK, (i * CELL_SIZE + CELL_SIZE // 2, CELL_SIZE // 2),
                                     (i * CELL_SIZE + CELL_SIZE // 2, HEIGHT - CELL_SIZE // 2), 3)
                    winning_cells = [(0, i), (1, i), (2, i)]
                    if turn == 'X':
                        kazanan_o = True
                    if turn == 'O':
                        kazanan_x = True
                    sayac = 1
                    game_over = True
            # Sol dan çapraz yapınca
            if board[0][0] == board[1][1] == board[2][2] != '':
                pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, CELL_SIZE // 2),
                                 (WIDTH - CELL_SIZE // 2, HEIGHT - CELL_SIZE // 2), 3)
                winning_cells = [(0, 0), (1, 1), (2, 2)]
                if turn == 'X':
                    kazanan_o = True
                if turn == 'O':
                    kazanan_x = True
                sayac = 1
                game_over = True
            # Sağdan çapraz yapınca
            elif board[0][2] == board[1][1] == board[2][0] != '':
                pygame.draw.line(screen, BLACK, (CELL_SIZE // 2, HEIGHT - CELL_SIZE // 2),
                                 (WIDTH - CELL_SIZE // 2, CELL_SIZE // 2), 3)
                winning_cells = [(0, 2), (1, 1), (2, 0)]
                if turn == 'X':
                    kazanan_o = True
                if turn == 'O':
                    kazanan_x = True
                sayac = 1
                game_over = True
        if sayac == 0:
            if board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2] != '':
                game_over_draw = True

                # Çizgi
        if winning_cells:
            start_row, start_col = winning_cells[0]
            end_row, end_col = winning_cells[-1]
            start_x = start_col * CELL_SIZE + CELL_SIZE // 2
            start_y = start_row * CELL_SIZE + CELL_SIZE // 2
            end_x = end_col * CELL_SIZE + CELL_SIZE // 2
            end_y = end_row * CELL_SIZE + CELL_SIZE // 2

            delta_x = end_x - start_x
            delta_y = end_y - start_y
            line_length = int(CELL_SIZE * 0.3)  # Çizgi uzunluğunu belirle (karoların 1.5 katı)

            start_x -= int(delta_x * (line_length / (2 * CELL_SIZE)))
            start_y -= int(delta_y * (line_length / (2 * CELL_SIZE)))
            end_x += int(delta_x * (line_length / (2 * CELL_SIZE)))
            end_y += int(delta_y * (line_length / (2 * CELL_SIZE)))

            for i in range(1, 6):
                alpha = 255 - (i * 100)  # Kenarların şeffaflık değeri
                color = (0, 0, 0, alpha)  # Çizgi rengi ve alfa değeri
                width = 11 - i  # Çizgi kalınlığı
                pygame.draw.line(screen, GREEN, (start_x, start_y), (end_x, end_y), width)

        if game_over:
            font = pygame.font.Font(None, 36)
            text = font.render("Oyun Bitti!", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2.4 - text.get_height()))
            if kazanan_x:
                text = font.render("X Kazandı!", True, RED)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height()))
            if kazanan_o:
                text = font.render("O Kazandı!", True, BLUE)
                screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height()))
            text = font.render("Oynamak için Tıklayın", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2.4 + text.get_height()))

        if game_over_draw:
            font = pygame.font.Font(None, 36)
            text = font.render("Oyun Bitti!", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2.6 - text.get_height() // 3))
            text = font.render("Beraberlik!", True, GRAY)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2.2 + text.get_height() // 4))
            text = font.render("Oynamak için Tıklayın", True, BLACK)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + text.get_height()))

        pygame.display.flip()

    pygame.quit()