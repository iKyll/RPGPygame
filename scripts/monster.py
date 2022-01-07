from scripts.character import Character
import pygame

import random
import json
import sys
import os

class Monster(Character):
    def __init__(self, game, type):
        super().__init__(type)
        self.game = game
        self.type = type

        self.sprite_sheet = super().getSpriteSheet()
        self.image = super().get_img(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.position = [0,0]
        self.old_position = self.position.copy()
        self.speed = 2

        self.level = None
        self.health = None
        self.damage = None
        self.exp_value = None
        self.coin_value = None

        self.init_stats()

    def init_stats(self):
        json_reader = open(os.path.join(sys.path[0], "config\\monster.json"), "r")
        monster_id = json_reader.read()
        monster_id = json.loads(monster_id)

        if self.type == "slime":
            self.level = monster_id.slime.level
            self.health = random.randint(monster_id.slime.health[0], monster_id.slime.health[1])
            self.damage = random.randint(monster_id.slime.damage[0], monster_id.slime.damage[1])
            self.exp_value = random.randint(monster_id.slime.exp_value[0], monster_id.slime.exp_value[1])
            self.coin_value = random.randint(monster_id.slime.coin_value[0], monster_id.slime.coin_value[1])
            
        elif self.type == "goblin":
            self.level = monster_id.goblin.level
            self.health = random.randint(monster_id.goblin.health[0], monster_id.goblin.health[1])
            self.damage = random.randint(monster_id.goblin.damage[0], monster_id.goblin.damage[1])
            self.exp_value = random.randint(monster_id.goblin.exp_value[0], monster_id.goblin.exp_value[1])
            self.coin_value = random.randint(monster_id.goblin.coin_value[0], monster_id.goblin.coin_value[1])
 
        elif self.type == "golem":
            self.level = monster_id.golem.level
            self.health = random.randint(monster_id.golem.health[0], monster_id.golem.health[1])
            self.damage = random.randint(monster_id.golem.damage[0], monster_id.golem.damage[1])
            self.exp_value = random.randint(monster_id.golem.exp_value[0], monster_id.golem.exp_value[1])
            self.coin_value = random.randint(monster_id.golem.coin_value[0], monster_id.golem.coin_value[1])
 
        elif self.type == "orc":
            self.level = monster_id.orc.level
            self.health = random.randint(monster_id.orc.health[0], monster_id.orc.health[1])
            self.damage = random.randint(monster_id.orc.damage[0], monster_id.orc.damage[1])
            self.exp_value = random.randint(monster_id.orc.exp_value[0], monster_id.orc.exp_value[1])
            self.coin_value = random.randint(monster_id.orc.coin_value[0], monster_id.orc.coin_value[1])
 
