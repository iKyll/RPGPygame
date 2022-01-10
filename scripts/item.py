import sys
import os

import pygame

class Item:
    def __init__(self, game, name,x,y):
        self.game = game
        self.name = name

        self.sprite_sheet = pygame.image.load(os.path.join(sys.path[0], f"assets\\item\\{self.name}.png"))
        self.img = self.get_img(x,y)


    def get_img(self, x, y) -> pygame.Surface:
        image = pygame.Surface([38, 38])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 38, 38))
        return image