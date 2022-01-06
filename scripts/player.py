from scripts.entity import Entity
import pygame
import sys
import os

class Player(Entity):
    def __init__(self, game):
        super().__init__("player")
        self.game = game

        self.sprite_sheet = super().getSpriteSheet()
        self.image = super().get_img(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.key_pressed = {}

        self.speed = 2

    def Update(self):         
        if self.key_pressed.get(pygame.K_RIGHT):
            self.rect.x += self.speed
        elif self.key_pressed.get(pygame.K_LEFT):
            self.rect.x -= self.speed
        