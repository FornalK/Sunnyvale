import pygame
from settings import *
from objects.characters.Player import Player
from objects.world_elements.Wall import Wall


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        # later drawing elements and creation should be wrapped in a function
        player = Player(WINDOW_WIDTH / 2 - PLAYER_WIDTH / 2,
                        WINDOW_HEIGHT - PLAYER_HEIGHT - 20,
                        PLAYER_WEIGHT,
                        PLAYER_HEIGHT,
                        PLAYER_WEIGHT,
                        PLAYER_MAX_SPEED)

        right_wall = Wall(WINDOW_WIDTH - 20,
                          0,
                          20,
                          WINDOW_HEIGHT - 20)

        left_wall = Wall(0,
                         0,
                         20,
                         WINDOW_HEIGHT - 20)

        ground = Wall(0,
                      WINDOW_HEIGHT - 20,
                      WINDOW_WIDTH,
                      20)

        walls = [right_wall, left_wall, ground]

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

            player_hitbox_surf = pygame.Surface(
                (player.get_width(), player.get_height()), pygame.SRCALPHA)
            player_hitbox_surf.fill((0, 0, 255, 25))
            player_hitbox = pygame.draw.rect(player_hitbox_surf, PLAYER_HITBOX_COLOR,
                             (0, 0, player.get_width(), player.get_height()), 4)
            self.screen.blit(
                player_hitbox_surf, (player.get_positionx(), player.get_positiony()))

            drawed_walls = []
            for wall in walls:
                drawed_wall = pygame.draw.rect(self.screen, WALL_TEXTURE_COLOR,
                                (wall.get_positionx(), wall.get_positiony(), wall.get_width(), wall.get_height()))
                drawed_walls.append(drawed_wall)

            # detecting collision
            # Cos jest nie tak. Mimo ze gracz styka sie tylko z podłożem przy starcie gry to pokazuje bez względu na umiejscowienie gracza,
            # ze styka on sie z lewa sciana
            """
            collide = player_hitbox.collidelistall(drawed_walls)
            if collide:
                print("walls id: " + str(collide))
            """
            pygame.display.update()



if __name__ == '__main__':
    main = Main()
    main.run()
