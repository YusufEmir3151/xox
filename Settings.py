import pygame
import methods

WIDTH = methods.WIDTH
HEIGHT = methods.HEIGHT
BLACK = methods.BLACK

def show_settings():
    global fullscreen, first_player, second_player
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ayarlar")

    font = pygame.font.Font(None, 36)
    title_text = font.render("Ayarlar", True, BLACK)

    fullscreen_text = font.render("Tam Ekran", True, BLACK)
    first_player_text = font.render("İlk Oyuncu", True, BLACK)
    start_game_text = font.render("Tamam", True, BLACK)

def toggle_fullscreen(screen):
    global WIDTH, HEIGHT
    if fullscreen:
        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))