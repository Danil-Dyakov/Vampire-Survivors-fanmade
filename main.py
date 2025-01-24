import sys
import pygame
from pygame import Surface
from pygame.time import Clock
from src.utilits.load_image import load_image
from src.utilits.load_level import load_level

FPS = 60

def main() -> None:
    pygame.init()
    pygame.display.set_caption('Vampire Survivors Fanmade v.1.0')

    size = 1920, 1080

    display_info = pygame.display.Info()
    pygame.display.set_mode((display_info.current_w, display_info.current_h))
    screen = pygame.display.set_mode(size)

    start_screen(screen)
    play(screen)
    terminate()

def start_screen(screen: Surface) -> None:
    clock = Clock()
    background = pygame.transform.scale(load_image('start_screen.png'), screen.get_size())
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

def play(screen: Surface) -> None:
    player, level_x, level_y = generate_level(load_level('level_1.txt'))
    clock = pygame.time.Clock()

    camera = Camera(screen.get_size())
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        screen.fill((0, 0, 255))
        camera.update(player)
        for sprite in all_sprites:
            camera.apply(sprite)
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

tile_images = {
    'wall': load_image('tree.png'),
    'empty': load_image('grass.png')
}

player_images = {
    'up': load_image('hero_up.png'),
    'down': load_image('hero_down.png'),
    'left': load_image('hero_left.png'),
    'right': load_image('hero_right.png')
}

tile_width = tile_height = 50

class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_images['down']
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
        self.speed = 5
        self.direction = 'down'

    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = 'left'
            self.image = player_images['left']
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = 'right'
            self.image = player_images['right']
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = 'up'
            self.image = player_images['up']
        if keys[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = 'down'
            self.image = player_images['down']

player = None

all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                coords = x, y
    new_player = Player(*coords)
    return new_player, x, y

class Camera:
    def __init__(self, viewport_size):
        self.dx = 0
        self.dy = 0
        self._viewport_size = viewport_size

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - self._viewport_size[0] // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - self._viewport_size[1] // 2)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)