from time import time

import pygame
from pygame import Surface, key

from src.camera import Camera
from src.generate_level import generate_level
from src.groups import all_sprites
from src.utilits.load_level import load_level


def play(screen: Surface) -> None:
    player, level_x, level_y = generate_level(load_level('level_1.txt'))
    clock = pygame.time.Clock()

    camera = Camera(screen.get_size())
    speed = 5
    running = True
    frame_time = 0
    frame_start_time = time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        a = key.get_pressed()
        player.move(a)

        player.update(frame_time)
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)

        screen.fill((0, 0, 255))
        all_sprites.draw(screen)
        pygame.display.flip()

        frame_end_time = time()
        frame_time = frame_end_time - frame_start_time
        frame_start_time = frame_end_time
