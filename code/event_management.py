from objects.creatures.characters.Player import Player
from objects.world_elements.Wall import Wall

# Handle players behavior when collide with wall
def collision_with_wall(player, wall):
    # find x and y for all sites of players and walls hitbox
    player_up = player.get_positiony() - player.get_height() / 2
    player_bottom = player.get_positiony() + player.get_height() / 2
    player_left = player.get_positionx() - player.get_width() / 2
    player_right = player.get_positionx() + player.get_width() / 2

    wall_up = wall.get_positiony()
    wall_bottom = wall_up + wall.get_height()
    wall_left = player.get_positionx()
    wall_right = wall_left + wall.get_width()

    # calculate distances between possible connected walls
    distances = [abs(player_bottom - wall_up), abs(player_up - wall_bottom),
                 abs(player_left - wall_right), abs(player_right - wall_left)]

    # find which site of player and wall are connected
    min_dist_index = distances.index(min(distances))

    if min_dist_index == 0:
        player.change_in_air()
    elif min_dist_index == 1:
        player.set_positiony(player.get_positiony() + 50) #imitacja odbicia sie glowa od podloza
    elif min_dist_index == 2:
        player.set_act_speed(0)
        player.set_move_direction(1)
    elif min_dist_index == 3:
        player.set_act_speed(0)
        player.set_move_direction(-1)
    else:
        raise