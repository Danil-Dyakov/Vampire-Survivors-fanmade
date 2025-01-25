from src.player import Player
from src.tiles import Tile


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '?':
                Tile('swamp', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                coords = x, y
    new_player = Player(*coords)
    return new_player, x, y