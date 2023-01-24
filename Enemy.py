from random import randint
from Common import map_to_coords


class Enemy:
    def __init__(self, game):
        self.game = game
        
        self.map = [[0] for _ in range(game.height+1)]
        self.map[randint(game.height-len(game.player.map)+1,game.height)][0] = 1

        self.distance_to_roof = game.height - len(self.map) + 1
        self.coords = map_to_coords(self.map)
        self.pos_y = self.distance_to_roof
        self.pos_x = game.width
