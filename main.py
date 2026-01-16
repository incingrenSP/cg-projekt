import sys

import pygame

from src.debug import debug
from src.level import Level
from src.settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pling Pling Plong")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("black")
            self.clock.tick(FPS)
            debug(self.clock.get_fps())
            self.level.run()

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
