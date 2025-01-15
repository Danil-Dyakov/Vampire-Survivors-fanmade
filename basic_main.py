import os
import sys

import pygame
from pygame import Surface
from pygame.time import Clock
from utilits.load_image import load_image

FPS = 60


def main() -> None:
    pygame.init()
    pygame.display.set_caption('Игра «Жизнь Кикориков»')

    size = 1920, 1080

    display_info = pygame.display.Info()
    pygame.display.set_mode((display_info.current_w, display_info.current_h))
    screen = pygame.display.set_mode(size)

    start_screen(screen)


#    while True:
#        play(screen)
#        play_again = end_screen(screen)
#        if not play_again:
#            terminate()


def start_screen(screen: Surface) -> None:

    clock = Clock()
    background = pygame.transform.scale(load_image('start_screen.png'), screen.get_size())
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def play(screen: Surface) -> None:
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
