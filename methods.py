import pygame
# Pencere boyutları
WIDTH = 300
HEIGHT = 300

# Oyun tahtası boyutları
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (125, 125, 125)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0, 180)

# Kazanan belirleme
kazanan_x = False
kazanan_o = False
sayac = 0


fullscreen_checkbox = pygame.Rect(35, 100, 30, 30)
first_player_x_button = pygame.Rect(20, 150, 30, 30)
first_player_o_button = pygame.Rect(50, 150, 30, 30)
second_player_x_button = pygame.Rect(20, 200, 30, 30)
second_player_o_button = pygame.Rect(50, 200, 30, 30)
start_game_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 100, 100, 50)

global fullscreen, first_player, second_player
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ayarlar")

font = pygame.font.Font(None, 36)
title_text = font.render("Ayarlar", True, BLACK)

fullscreen_text = font.render("Tam Ekran", True, BLACK)
first_player_text = font.render("İlk Oyuncu", True, BLACK)
start_game_text = font.render("Tamam", True, BLACK)


