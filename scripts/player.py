from scripts.character import Character
import pygame
import sys
import os

class Player(Character):
    def __init__(self, game):
        super().__init__("player")
        self.game = game

        self.sprite_sheet = super().getSpriteSheet()
        self.image = super().get_img(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.images = {
            "up": super().get_img(0, 96),
            "down": super().get_img(0, 0),
            "right": super().get_img(0, 64),
            "left": super().get_img(0, 32)
        }

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.position = [114,196]
        self.old_position = self.position.copy()
        self.key_pressed = {}
        self.speed = 3

    def save_location(self): self.old_position = self.position.copy()

    def move_player(self, type):
        self.image = self.images[type]
        self.image.set_colorkey([0, 0, 0])
        if type == "up":
            self.position[1] -= self.speed
        elif type == "down":
            self.position[1] += self.speed
        elif type == "right":
            self.position[0] += self.speed
        elif type == "left":
            self.position[0] -= self.speed

    def move_back(self):
        self.position = self.old_position

    def checkCollisions(self):
        for sprite in self.game.map_manager.get_group().sprites():
            if sprite.feet.collidelist(self.game.map_manager.get_walls()) > -1:
                sprite.move_back()

    def Update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

        self.checkCollisions()
        