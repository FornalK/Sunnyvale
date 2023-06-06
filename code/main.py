import pygame
from settings import *
from objects.characters.Player import Player


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        # later drawing elements and creation should be wrapped in a function
        player = Player(WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2,
                        WINDOW_HEIGHT - PLAYER_HEIGHT,
                        PLAYER_WEIGHT,
                        PLAYER_HEIGHT,
                        PLAYER_WEIGHT,
                        PLAYER_MAX_SPEED)

        self.running = True
        while self.running:
            dt = self.clock.tick() / 1000
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.screen.fill(BACKGROUND)

            player.move_horizontal(keys, dt)

            player_hitbox = pygame.Surface(
                (player.get_width(), player.get_height()), pygame.SRCALPHA)
            player_hitbox.fill((0, 0, 255, 25))
            pygame.draw.rect(player_hitbox, PLAYER_HITBOX_COLOR,
                             (0, 0, player.get_width(), player.get_height()), 4)
            self.screen.blit(
                player_hitbox, (player.get_positionx(), player.get_positiony()))
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
