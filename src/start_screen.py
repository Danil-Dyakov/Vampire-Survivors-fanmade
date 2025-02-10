import pygame
from pygame import Surface
from pygame.time import Clock

from src.terminate import terminate
from src.utilits.load_image import load_image


def start_screen(screen: Surface) -> None:

    clock = Clock()
    FPS = 60
    background = pygame.transform.scale(load_image('start_screen.png'), screen.get_size())
    screen.blit(background, (0, 0))
    pygame.mixer.music.load("assets/music/Faint Glow.mp3")
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                return
        pygame.display.flip()
        clock.tick(FPS)
