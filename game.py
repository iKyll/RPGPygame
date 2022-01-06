from scripts.map_manager import MapManager
from scripts.window import Window
from scripts.player import Player

class Game:
    def __init__(self):
        self.window = Window(self)
        self.player = Player(self)
        self.map_manager = MapManager(self)

    def Update(self):
        self.window.Update()
        self.map_manager.Update()
        self.player.Update()

    def run(self):
        while True:
            self.Update()

Game().run()