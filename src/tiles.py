import pygame

from src.groups import tiles_group, all_sprites, wall_group
from src.utilits.load_image import load_image

tile_images = {
    'wall': load_image('tree.png'),
    'empty': load_image('grass.png'),
    'chest': load_image('chest_closed.png')
}

tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if tile_type == "wall":
            wall_group.add(self)