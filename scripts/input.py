import pygame

class InputHandler():
    def __init__(self, game):
        self.game = game
        self.pressed = {}

    def Update(self):
        if self.pressed.get(pygame.K_UP):
            self.game.player.move_player("up")
        elif self.pressed.get(pygame.K_DOWN):
            self.game.player.move_player("down")
        elif self.pressed.get(pygame.K_RIGHT):
            self.game.player.move_player("right")
        elif self.pressed.get(pygame.K_LEFT):
            self.game.player.move_player("left")

        