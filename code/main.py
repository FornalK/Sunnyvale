import pygame
from event_management import *
from settings import *
from objects.creatures.characters.Player import Player
from objects.world_elements.Wall import Wall
from support import *

from editor import Editor

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
        self.clock = pygame.time.Clock()
        self.running = False

        self.graphics = import_folder_dict('../graphics/editor')

        self.editor = Editor(self.graphics)

    def run(self):
        """
        # later drawing elements and creation should be wrapped in a function
        player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT -
                        (PLAYER_HEIGHT / 2) - 20)

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

        platform1 = Wall(200,
                         WINDOW_HEIGHT - 100,
                         300,
                         20)

        platform2 = Wall(800,
                         WINDOW_HEIGHT - 350,
                         400,
                         20)

        walls = [right_wall, left_wall, ground, platform1, platform2]
        """
        self.running = True
        while self.running:
            dt = self.clock.tick() / 1000

            """
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            self.screen.fill(BACKGROUND)

            player_hitbox = pygame.draw.rect(self.screen, PLAYER_HITBOX_COLOR,
                                             (player.get_positionx() - player.get_width() / 2,
                                              player.get_positiony() - player.get_height() / 2,
                                              player.get_width(),
                                              player.get_height()),
                                             4)

            # draw center of the player object
            pygame.draw.circle(self.screen,
                               PLAYER_HITBOX_COLOR,
                               player.get_position(), 2)

            drawed_walls = []
            for wall in walls:
                drawed_wall = pygame.draw.rect(self.screen,
                                               WALL_TEXTURE_COLOR,
                                               (wall.get_positionx(),
                                                wall.get_positiony(),
                                                wall.get_width(),
                                                wall.get_height()))
                drawed_walls.append(drawed_wall)

                # draw center of the wall object
                pygame.draw.circle(self.screen,
                                   (0, 0, 0),
                                   wall.get_position(), 2)

            # set default that player is in air and then check if there is any collision
            player.in_air = True

            # detecting collision between player and walls
            colliding_walls = player_hitbox.collidelistall(drawed_walls)
            for wall_index in colliding_walls:
                collision_with_wall(player, walls[wall_index])

            player.move_horizontal(keys, dt)
            player.move_up(keys, dt)
            
            """

            self.editor.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    main = Main()
    main.run()
