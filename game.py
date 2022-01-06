from scripts.window import Window
from scripts.player import Player

class Game:
    def __init__(self):
        self.window = Window(self)
        self.player = Player(self)

    def Update(self):
        self.window.Update()
        self.player.Update()

    def run(self):
        while True:
            self.Update()

Game().run()