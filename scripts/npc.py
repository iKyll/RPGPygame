from scripts.character import Character
import pygame

class NPC(Character):
    def __init__(self, game, type, name):
        super().__init__(type)
        self.game = game
        self.type = type
        self.name = name

        self.sprite_sheet = super().getSpriteSheet()
        self.image = super().get_img(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
