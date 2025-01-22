import pygame
from pygame.key import ScancodeWrapper

from src.groups import movable_group, all_sprites
from src.tiles import player_image, tile_width, tile_height


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int):
        super().__init__(movable_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.coordinates = [self.rect.x, self.rect.y]
        self.speed = [0, 0]
        self.max_speed = 10000

    def move(self, key_pressed: ScancodeWrapper):
        if key_pressed[pygame.K_LEFT]:
            self.speed[0] = -self.max_speed
        if key_pressed[pygame.K_RIGHT]:
            self.speed[0] = self.max_speed
        if key_pressed[pygame.K_UP]:
            self.speed[1] = -self.max_speed
        if key_pressed[pygame.K_DOWN]:
            self.speed[1] = self.max_speed

    def update(self, frame_time: int) -> None:
        self.coordinates[0] += self.speed[0] * frame_time
        self.coordinates[1] += self.speed[1] * frame_time
        self.rect.x = self.coordinates[0]
        self.rect.y = self.coordinates[1]

