import pygame

from src import player
from src.groups import wall_group, chest_group, all_sprites
from src.utilits.load_image import load_image

chest_images = {
    "opened": load_image("chest_opened.png"),
    "closed": load_image("chest_closed.png")
}


class Chest(pygame.sprite.Sprite):
    def __init__(self, x_pos: int, y_pos: int) -> None:
        super().__init__(all_sprites, wall_group, chest_group)
        self.image = chest_images["opened"]
        self.rect = self.image.get_rect().move(x_pos, y_pos)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def check_opening(self):
        if self.image == chest_images["opened"] and player.coin == True:
            self.image = chest_images["closed"]