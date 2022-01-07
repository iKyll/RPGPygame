from scripts.map_manager import MapManager
from scripts.window import Window
from scripts.player import Player
from scripts.input import InputHandler

import pygame

class Game:
    def __init__(self):
        self.window = Window(self)
        self.player = Player(self)
        self.map_manager = MapManager(self)
        self.input_handler = InputHandler(self)

        self.clock = pygame.time.Clock()

    def Update(self):
        self.window.Update()
        self.map_manager.Update()
        self.input_handler.Update()
        self.player.Update()

        self.clock.tick(60)

    def run(self):
        while True:
            self.Update()

Game().run()