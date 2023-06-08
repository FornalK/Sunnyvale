from objects.creatures.characters.Player import Player
from objects.world_elements.Wall import Wall


def collision_with_wall(player, wall):
    if not wall.get_rotation(): # wall is vertical
        player.set_act_speed(0)

        # check on which side of the wall the player is
        if player.get_positionx() > wall.get_positionx():
            player.set_positionx(player.get_positionx() + 1)
        else:
            player.set_positionx(player.get_positionx() - 1)

    else: # wall is horizontal
        # check on which side of the wall the player is
        if player.get_positiony() < wall.get_positiony():
            player.change_in_air()
            # Gracz stoi na obiekcie i powstrzymuje go to przed spadkiem swobodnym w dół
            # należy rozważyć czy przy skoku kiedy gracz będzie lądował na powierzchni to czy nie powinien wytracać
            # w penwym stopniu swojej prędkości
        else:
            pass
            # Gracz odbija się "głową" od powierzchni sciany. Należy rozważyć czy nie zaimplementować mechaniki
            # odbicia (np, dodanie predkosci do opadania)
