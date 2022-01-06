import pygame
import sys
import os

class Entity(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        super().__init__()

        self.sprite_sheet = sprite_sheet

    def getSpriteSheet(self):
        sprite_sheet = pygame.image.load(os.path.join(sys.path[0], f"assets\\sprites\\{self.sprite_sheet}.png"))
        return sprite_sheet
    
    def get_img(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image