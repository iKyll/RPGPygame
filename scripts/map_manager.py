import os
import sys
from dataclasses import dataclass
from typing import List

import pygame
import pyscroll
import pytmx


@dataclass
class Map:
    map: str
    walls: List[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data = pytmx.TiledMap

class MapManager:
    def __init__(self, game):
        self.game = game

        self.maps = dict()
        self.current_map = "temp_map"

        self.register_map("temp_map")

    def register_map(self, name):
        tmx_data = pytmx.until_pygame.load_pygame(os.path.join(sys.path[0], f"assets\\maps\\{name}.tmx"))
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthografic.BufferedRenderer(map_data, self.game.window.window.get_size())
        map_layer.zoom = 2

        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.game.player)

        self.maps[name] = Map(name, walls, group, tmx_data)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_player(self, name):
        point = self.get_object(name)
        self.game.player.rect.x = point.x
        self.game.player.rect.y = point.y


    def draw(self):
        self.get_group().draw(self.game.window.window)
        self.get_group().center(self.game.player.rect.center)

    def Update(self):
        self.get_group().update()
