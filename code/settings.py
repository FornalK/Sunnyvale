# general setup
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 700
TILE_SIZE = 32

# colors
BACKGROUND = (127, 127, 127)
PLAYER_HITBOX_COLOR = (0, 0, 255)
WALL_TEXTURE_COLOR = (252, 186, 3)
LINE_COLOR = (0, 0, 0)

# player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 170
PLAYER_WEIGHT = 65
PLAYER_MAX_SPEED = 200
PLAYER_ACCELERATION = 50
PLAYER_RETARDATION = 250
PLAYER_JUMP_MAX_SPEED = 200
PLAYER_NUM_JUMP = 2

# types
TYPE_PLAYER = 0
TYPE_MOB = 1
TYPE_MORTAL_NPC = 2
TYPE_IMMORTAL_NPC = 3

# constant values
GRAVITY = 200

# editor
EDITOR_DATA = {
    0: {'style': 'player', 'type': 'creature', 'menu_surf': '../graphics/preview/player.png', 'editor': '../graphics/editor/player.png'},
    1: {'style': 'background', 'type': 'object', 'menu_surf': '../graphics/preview/background.png', 'editor': '../graphics/editor/background.png' },
    2: {'style': 'terrain', 'type': 'tile', 'menu_surf': '../graphics/preview/terrain.png', 'editor': '../graphics/editor/terrain.png' },
}

EDITOR_DATA_MIN_INDEX = 0
EDITOR_DATA_MAX_INDEX = 2
