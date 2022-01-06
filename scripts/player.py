from scripts.entity import Entity
import pygame
import sys
import os

class Player(Entity):
    def __init__(self, game):
        super().__init__()
        self.game = game

        self.sprite_sheet = pygame.image.load(os.path.join(sys.path[0], "assets\\sprites\\player.png"))
        self.image = self.get_img(0, 0)
        self.rect = self.image.get_rect()

        self.speed = 2
        self.key_pressed = {}

    def get_img(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0,0), (x, y, 32, 32))
        return image

    def Update(self):         
        if self.key_pressed.get(pygame.K_RIGHT):
            self.rect.x += self.speed
        elif self.key_pressed.get(pygame.K_LEFT):
            self.rect.x -= self.speed
        