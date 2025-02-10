import pygame
from pygame import Surface

from src.camera import Camera
from src.generate_level import generate_level
from src.groups import all_sprites
from src.coin import Coin
from src.utilits.load_level import load_level



def play(screen: Surface, FPS=60) -> None:
    player, level_x, level_y = generate_level(load_level('level_1.txt'))
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/music/The Field of Hopes and Dreams.mp3")
    camera = Camera(screen.get_size())
    running = True
    coin_count = 0

    # pygame.mixer.music.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        if player.coin:
            coin_count += 1
        coin = Coin(screen, str(coin_count))
        coin.move(keys)
        coin.animation()



        screen.fill((0, 0, 255))
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        coin.coin_counter()
        screen.blit(coin.image, coin.image_coords)
        pygame.display.flip()
        clock.tick(FPS)
