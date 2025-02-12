import pygame
from pygame import Surface

from src.play import play
from src.terminate import terminate
from src.utilits.load_image import load_image


def end_screen(screen: Surface):
    pygame.mixer.music.load("assets/music/Determination.mp3")
    pygame.mixer.music.play()
    running = True
    img = load_image("game_over.png")
    img_coords = (0, 0)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.K_ESCAPE:
                terminate()
            elif event.type == pygame.K_KP_ENTER:
                play(screen)

        screen.blit(img, img_coords)