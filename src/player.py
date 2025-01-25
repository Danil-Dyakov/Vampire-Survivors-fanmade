import pygame
from pygame.sprite import collide_rect, spritecollideany

from src.groups import player_group, all_sprites, wall_group
from src.tiles import tile_width, tile_height
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
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_images['down']
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 5
        self.cooldown = 0
        self.coldown_time = 3
        self.direction = 'down'

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = 'left'
            if self.image == player_images['left'] and self.cooldown == 5:
                self.image = player_images['left2']
                self.cooldown = 0
            elif self.image == player_images['left2'] and self.cooldown == 5:
                self.image = player_images['left3']
                self.cooldown = 0
            elif self.image == player_images['left3'] and self.cooldown == 5:
                self.image = player_images['left4']
                self.cooldown = 0
            elif self.image == player_images['left4'] and self.cooldown == 5:
                self.image = player_images['left']
                self.cooldown = 0
            elif self.cooldown < 5:
                self.cooldown += 1
            elif self.image != player_images['left'] and self.image != player_images['left2'] and self.image != \
                    player_images['left3'] and self.image != player_images['left4']:
                self.image = player_images['left']
                self.cooldown = 0
            if spritecollideany(self, wall_group) is not None:
                self.rect.x += self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 'right'
            if self.image == player_images['right'] and self.cooldown == self.coldown_time:
                self.image = player_images['right2']
                self.cooldown = 0
            elif self.image == player_images['right2'] and self.cooldown == self.coldown_time:
                self.image = player_images['right3']
                self.cooldown = 0
            elif self.image == player_images['right3'] and self.cooldown == self.coldown_time:
                self.image = player_images['right4']
                self.cooldown = 0
            elif self.image == player_images['right4'] and self.cooldown == self.coldown_time:
                self.image = player_images['right']
                self.cooldown = 0
            elif self.cooldown < self.coldown_time:
                self.cooldown += 1
            elif self.image != player_images['right'] and self.image != player_images['right2'] and self.image != \
                    player_images['right3'] and self.image != player_images['right4']:
                self.image = player_images['right']
                self.cooldown = 0
            if spritecollideany(self, wall_group) is not None:
                self.rect.x -= self.speed

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = 'up'
            if self.image == player_images['up'] and self.cooldown == self.coldown_time:
                self.image = player_images['up2']
                self.cooldown = 0
            elif self.image == player_images['up2'] and self.cooldown == self.coldown_time:
                self.image = player_images['up3']
                self.cooldown = 0
            elif self.image == player_images['up3'] and self.cooldown == self.coldown_time:
                self.image = player_images['up4']
                self.cooldown = 0
            elif self.image == player_images['up4'] and self.cooldown == self.coldown_time:
                self.image = player_images['up']
                self.cooldown = 0
            elif self.cooldown < self.coldown_time:
                self.cooldown += 1
            elif self.image != player_images['up'] and self.image != player_images['up2'] and self.image != \
                    player_images['up3'] and self.image != player_images['up4']:
                self.image = player_images['up']
                self.cooldown = 0
            if spritecollideany(self, wall_group) is not None:
                self.rect.y += self.speed

        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = 'down'
            if self.image == player_images['down'] and self.cooldown == self.coldown_time:
                self.image = player_images['down2']
                self.cooldown = 0
            elif self.image == player_images['down2'] and self.cooldown == self.coldown_time:
                self.image = player_images['down3']
                self.cooldown = 0
            elif self.image == player_images['down3'] and self.cooldown == self.coldown_time:
                self.image = player_images['down4']
                self.cooldown = 0
            elif self.image == player_images['down4'] and self.cooldown == self.coldown_time:
                self.image = player_images['down']
                self.cooldown = 0
            elif self.cooldown < self.coldown_time:
                self.cooldown += 1
            elif self.image != player_images['down'] and self.image != player_images['down2'] and self.image != \
                    player_images['down3'] and self.image != player_images['down4']:
                self.image = player_images['down']
                self.cooldown = 0
            if spritecollideany(self, wall_group) is not None:
                self.rect.y -= self.speed
