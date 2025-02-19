import pygame
from pygame import Surface

from src.main_processes.play import play
from src.main_processes.terminate import terminate
from src.utilits.load_image import load_image


def end_screen(screen: Surface):
    pygame.mixer.music.load("assets/music/Determination.mp3")

    ending = True
    img = load_image("game_over.png")
    img_coords = (0, 0)
    screen.fill((0, 0, 0))
    pygame.mixer.music.play()

    while ending:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ending = False
            elif event.type == pygame.K_ESCAPE:
                terminate()
            elif event.type == pygame.K_KP_ENTER:
                play(screen)

        screen.blit(img, img_coords)