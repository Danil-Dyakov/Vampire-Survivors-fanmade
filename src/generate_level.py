from src.chest import Chest
from src.player import Player
from src.tiles import Tile


def generate_level(level):
    new_player, x, y = None, None, None
    chests = []
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '!':
                Chest(x, y)
                chest = Chest(x, y)
                chests.append(chest)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player_coordinates = x, y
    new_player = Player(*new_player_coordinates)
    return new_player, x, y, chests