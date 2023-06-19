import pygame, sys
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from settings import *

from editor_menu import EditorMenu


class Editor:
    def __init__(self, graphics):
        # main setup
        self.display_surface = pygame.display.get_surface()
        self.canvas_data = {}

        # imports
        self.surfs = graphics

        # navigation
        self.origin = vector()
        self.pan_active = False
        self.pan_offset = vector()

        # support lines
        self.support_line_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.support_line_surf.set_colorkey('green')
        self.support_line_surf.set_alpha(30)

        # selection
        #    current index of the world element we want to draw
        self.selection_index = 0

        #    coordinates of last selected cell in editor
        self.last_selected_cell = None

        # editor menu instance
        self.menu = EditorMenu()

    # support
    def get_current_cell(self):
        distance_to_origin = vector(mouse_pos()) - self.origin

        if distance_to_origin.x > 0:
            col = int(distance_to_origin.x / TILE_SIZE)
        else:
            col = int(distance_to_origin.x / TILE_SIZE) - 1

        if distance_to_origin.y > 0:
            row = int(distance_to_origin.y / TILE_SIZE)
        else:
            row = int(distance_to_origin.y / TILE_SIZE) - 1

        return col, row

    # input
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pan_input(event)
            self.selection_hotkeys(event)
            self.canvas_add()

    def pan_input(self, event):

        # middle mouse button pressed / released
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
            self.pan_active = True
            self.pan_offset = vector(mouse_pos()) - self.origin

        if not mouse_buttons()[1]:
            self.pan_active = False

        # mouse wheel
        if event.type == pygame.MOUSEWHEEL:
            if pygame.key.get_pressed()[pygame.K_LCTRL]:
                self.origin.y -= event.y * 50
            else:
                self.origin.x -= event.y * 50

        # panning update
        if self.pan_active:
            self.origin = vector(mouse_pos()) - self.pan_offset

    def selection_hotkeys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.selection_index += 1
            if event.key == pygame.K_LEFT:
                self.selection_index -= 1
        self.selection_index = max(EDITOR_DATA_MIN_INDEX,
                                   min(self. selection_index, EDITOR_DATA_MAX_INDEX))

    def canvas_add(self):
        # if mouse_buttons()[0] and not self.menu.menu_rect.collidepoint(mouse_pos()):
        if mouse_buttons()[0]:
            current_cell = self.get_current_cell()

            if current_cell != self.last_selected_cell:
                if current_cell in self.canvas_data:
                    self.canvas_data[current_cell].add_id(self.selection_index)
                else:
                    self.canvas_data[current_cell] = CanvasTile(self.selection_index)
                self.last_selected_cell = current_cell
    # drawing
    def draw_tile_lines(self):
        cols = WINDOW_WIDTH // TILE_SIZE
        rows = WINDOW_HEIGHT// TILE_SIZE

        origin_offset = vector(
            x = self.origin.x - int(self.origin.x / TILE_SIZE) * TILE_SIZE,
            y = self.origin.y - int(self.origin.y / TILE_SIZE) * TILE_SIZE)

        self.support_line_surf.fill('green')

        for col in range(cols + 1):
            x = origin_offset.x + col * TILE_SIZE
            pygame.draw.line(self.support_line_surf,LINE_COLOR, (x,0), (x,WINDOW_HEIGHT))

        for row in range(rows + 1):
            y = origin_offset.y + row * TILE_SIZE
            pygame.draw.line(self.support_line_surf,LINE_COLOR, (0,y), (WINDOW_WIDTH,y))

        self.display_surface.blit(self.support_line_surf,(0,0))

    def draw_tiles(self):
        for cell_pos, tile in self.canvas_data.items():
            pos = self.origin + vector(cell_pos) * TILE_SIZE

            if tile.has_terrain:
                new_surf = self.surfs['terrain']
                self.display_surface.blit(new_surf, pos)

            elif tile.objects:
                # its bad, only temporary 
                new_surf = self.surfs['player']
                self.display_surface.blit(new_surf, pos)

            else:
                new_surf = self.surfs['background']
                self.display_surface.blit(new_surf, pos)



            # enemies (for later)

    def run(self, dt):
        self.event_loop()

        # drawing
        self.display_surface.fill('white')
        self.draw_tile_lines()
        self.draw_tiles()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)
        self.menu.display(self.selection_index)

class CanvasTile:
    editor_data_styles = {key: value['style'] for key, value in EDITOR_DATA.items()}
    def __init__(self, tile_id):
        self.has_terrain = False
        self.objects = []

        self.add_id(tile_id)

    def add_id(self, tile_id):
        if self.editor_data_styles[tile_id] == 'player':
            self.objects.append(tile_id)
        elif self.editor_data_styles[tile_id] == 'background':
            pass
        elif self.editor_data_styles[tile_id] == 'terrain':
            self.has_terrain = True
