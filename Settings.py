import pygame
import methods
import data
WIDTH = methods.WIDTH
HEIGHT = methods.HEIGHT
BLACK = methods.BLACK
fullscreen = data.fullscreen
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



