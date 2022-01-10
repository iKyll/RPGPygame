import pygame
import time
import sys

from pygame.locals import *

class Window():
    def __init__(self, game):
        pygame.init()

        self.game = game
        self.window = pygame.display.set_mode((1280, 720))

        self.dt = None
        self.ltime = time.time()

        pygame.display.set_caption("WeshMaGueule")
        
    def change_resolution(self, resolution: tuple) -> None:
        self.window = pygame.display.set_mode(resolution)

    def Update(self):
        self.dt = time.time() - self.ltime
        self.dt *= 60
        self.ltime = time.time()

        self.game.player.save_location()
        self.game.map_manager.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.game.input_handler.pressed[event.key] = True

            elif event.type == pygame.KEYUP:
                self.game.input_handler.pressed[event.key] = False
        
        pygame.display.flip()
