import pygame
import sys

class Window():
    def __init__(self, game):
        pygame.init()

        self.game = game
        self.window = pygame.display.set_mode((1280, 720))

        pygame.display.set_caption("WeshMaGueule")
        
    def change_resolution(self, resolution: tuple):
        self.window = pygame.display.set_mode(resolution)

    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.game.player.key_pressed[event.key] = True
        pygame.display.flip()
