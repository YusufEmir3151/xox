import methods
import pygame

def toggle_fullscreen(screen):
    if screen.get_flags() & pygame.FULLSCREEN:
        pygame.display.set_mode((methods.WIDTH, methods.HEIGHT))
    else:
        pygame.display.set_mode((methods.WIDTH, methods.HEIGHT), pygame.FULLSCREEN)


