import pygame
from settings import *


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = False
    def run(self):
        self.running = True
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()

