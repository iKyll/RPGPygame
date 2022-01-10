from scripts.character import Character
import pygame
import math
import json
import sys
import os

class Player(Character):
    def __init__(self, game):
        super().__init__("player")
        self.game = game

        self.sprite_sheet = super().getSpriteSheet()
        self.image = super().get_img(0, 0).convert()
        self.image.set_colorkey([0,0,0])
        self.rect = self.image.get_rect()
        self.images = {
            "up": super().get_img(0, 96),
            "down": super().get_img(0, 0),
            "right": super().get_img(0, 64),
            "left": super().get_img(0, 32)
        }

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.position = [0,0]
        self.old_position = self.position.copy()
        self.key_pressed = {}
        self.default_speed = 3

        self.max_health = None
        self.health = None
        self.damage = None
        self.speed = self.default_speed
        self.max_mana = None
        self.mana = None

        self.helmet = None
        self.chestplate = None
        self.boots = None
        self.ring = None
        self.sword = None
        self.shield = None

        self.spells = [None, None, None]
        self.isFighting = False
        self.autoDamage = self.damage
        self.boost_turn = None
        self.spell_id = self.init_spells()

        self.inventory = {}

    def save_location(self) -> None: self.old_position = self.position.copy()

    def cast_spell(self, monster, name) -> None:
        if name == "fireball":
            if self.mana >= self.spell_id[name]['cost']:
                monster.take_damage(math.ceil(self.damage * self.spell_id[name]['damage']))
        elif name == "heal":
            if self.mana >= self.spell_id[name]["cost"]:
                self.health += self.spell_id[name]['value']
                if self.health > self.max_health:
                    self.health = self.max_health
        elif name == "cursed":
            if self.mana >= self.spell_id[name]["cost"]:
                monster.cursed = True
                monster.cursed_turn = 2
        elif name == "boost":
            if self.mana >= self.spell_id[name]["cost"]:
                self.autoDamage += math.ceil(self.damage * 0.25)
                self.boost_turn = 2
        elif name == "lightning_bolt":
            if self.mana >= self.spell_id[name]["cost"]:
                monster.take_damage(math.ceil(self.damage * 0.1))
                monster.paralyzed = True

    def change_pos(self, x, y) -> None:
        self.position[0] = x
        self.position[1] = y

        self.save_location()

    def move_player(self, type) -> None:
        self.image = self.images[type].convert()
        self.image.set_colorkey([0, 0, 0])
        if type == "up":
            self.position[1] -= self.speed * self.game.window.dt
        elif type == "down":
            self.position[1] += self.speed * self.game.window.dt
        elif type == "right":
            self.position[0] += self.speed * self.game.window.dt
        elif type == "left":
            self.position[0] -= self.speed * self.game.window.dt

    def move_back(self) -> None:
        self.position = self.old_position

    def checkCollisions(self) -> None:
        for sprite in self.game.map_manager.get_group().sprites():
            if sprite.feet.collidelist(self.game.map_manager.get_walls()) > -1:
                sprite.move_back()

    def init_spells(self) -> dict:
        json_reader = open(os.path.join(sys.path[0], "config\\monster.json"), "r")
        spells_id = json_reader.read()
        spells_id = json.loads(spells_id)
        return spells_id

    def Update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

        self.checkCollisions()
        