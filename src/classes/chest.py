import pygame

from src.other.groups import all_sprites, wall_group, chest_group
from src.utilits.load_image import load_image

chest_images = {
    "opened": load_image("chest_opened.png"),
    "closed": load_image("chest_closed.png")
}

tile_width = tile_height = 50


class Chest(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int) -> None:
        super().__init__(all_sprites, wall_group, chest_group)
        self.image = chest_images["closed"]
        self.rect = self.image.get_rect().move(tile_width * x_pos, tile_height * y_pos)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.check = False

    def check_opening(self, player):
        if self.image == chest_images["closed"] and player.loot:
            self.image = chest_images["opened"]
            self.check = True
        else:
            self.check = False
        return self.check