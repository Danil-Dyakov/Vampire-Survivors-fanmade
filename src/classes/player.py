import pygame
from pygame.sprite import spritecollideany

from src.other.groups import player_group, all_sprites, wall_group, chest_group
from src.classes.tiles import tile_width, tile_height
from src.utilits.load_image import load_image

player_images = {
    'up': load_image('hero_up.png'),
    'up2': load_image('hero_up2.png'),
    'up3': load_image('hero_up.png'),
    'up4': load_image('hero_up3.png'),
    'down': load_image('hero_down.png'),
    'down2': load_image('hero_down2.png'),
    'down3': load_image('hero_down.png'),
    'down4': load_image('hero_down3.png'),
    'left': load_image('hero_left.png'),
    'left2': load_image('hero_left2.png'),
    'left3': load_image('hero_left.png'),
    'left4': load_image('hero_left3.png'),
    'right': load_image('hero_right.png'),
    'right2': load_image('hero_right2.png'),
    'right3': load_image('hero_right.png'),
    'right4': load_image('hero_right3.png')
}

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(player_group, all_sprites)
        self.image = player_images['down']
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 5
        self.cooldown = 0
        self.coldown_time = 3
        self.direction = 'down'
        self.coin = False

    def move(self, keys) -> None:
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = 'left'

            self.animation(self.direction)

            # self.loot(check)

            if spritecollideany(self, wall_group) is not None:
                self.rect.x += self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 'right'

            self.animation(self.direction)

            # self.loot(check)

            if spritecollideany(self, wall_group) is not None:
                self.rect.x -= self.speed

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = 'up'

            self.animation(self.direction)

            # self.loot(check)

            if spritecollideany(self, wall_group) is not None:
                self.rect.y += self.speed

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = 'down'

            self.animation(self.direction)

            # self.loot(check)

            if spritecollideany(self, wall_group) is not None:
                self.rect.y -= self.speed

    def animation(self, side: str) -> None:
        if self.image == player_images[f'{side}'] and self.cooldown == self.coldown_time:
            self.image = player_images[f'{side}2']
            self.cooldown = 0
        elif self.image == player_images[f'{side}2'] and self.cooldown == self.coldown_time:
            self.image = player_images[f'{side}3']
            self.cooldown = 0
        elif self.image == player_images[f'{side}3'] and self.cooldown == self.coldown_time:
            self.image = player_images[f'{side}4']
            self.cooldown = 0
        elif self.image == player_images[f'{side}4'] and self.cooldown == self.coldown_time:
            self.image = player_images[f'{side}']
            self.cooldown = 0
        elif self.cooldown < self.coldown_time:
            self.cooldown += 1
        elif self.image != player_images[f'{side}'] and self.image != player_images[f'{side}2'] and self.image != \
                player_images[f'{side}3'] and self.image != player_images[f'{side}4']:
            self.image = player_images[f'{side}']
            self.cooldown = 0

    def loot(self, checking) -> bool:
        if spritecollideany(self, chest_group) is not None and checking:
            self.coin = True
            return True