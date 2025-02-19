import pygame

from src.utilits.load_image import load_image

coin_images = {
    "1": load_image("coin1.png"),
    "2": load_image("coin2.png"),
    "3": load_image("coin3.png"),
    "4": load_image("coin4.png"),
    "5": load_image("coin5.png"),
    "6": load_image("coin6.png"),
    "7": load_image("coin7.png"),
    "8": load_image("coin8.png")
}


class Coin(pygame.sprite.Sprite):
    def __init__(self, screen, coin_count: str):
        super().__init__()
        self.text_coords = (100, 175)
        self.image_coords = (50, 175)
        self.image = coin_images["1"]
        self.rect = self.image.get_rect().move(self.image_coords)
        self.coin_count = coin_count
        self.screen = screen
        self.speed = 5


    def coin_counter(self):
        coin_color = pygame.Color("yellow")
        coin_font = pygame.font.SysFont(None, 48)
        self.text = coin_font.render(self.coin_count, True, coin_color)
        self.screen.blit(self.text, self.text_coords)

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_s]:
            self.rect.y += self.speed

    def animation(self):
        if self.image == coin_images["1"]:
            self.image = coin_images["2"]
        elif self.image == coin_images["2"]:
            self.image = coin_images["3"]
        elif self.image == coin_images["3"]:
            self.image = coin_images["4"]
        elif self.image == coin_images["4"]:
            self.image = coin_images["5"]
        elif self.image == coin_images["5"]:
            self.image = coin_images["6"]
        elif self.image == coin_images["6"]:
            self.image = coin_images["7"]
        elif self.image == coin_images["7"]:
            self.image = coin_images["8"]
        elif self.image == coin_images["8"]:
            self.image = coin_images["1"]