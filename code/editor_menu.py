import pygame
from settings import *
from pygame.image import load
from editor import EDITOR_DATA


class EditorMenu:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.create_menu()
        self.create_data()

    def create_data(self):
        self.menu_surfs = {}
        for key, value in EDITOR_DATA.items():
            self.menu_surfs[key] = load(value['menu_surf'])

    def create_menu(self):
        # menu area
        size = 180 # menu size
        margin = 6
        self.topleft = [WINDOW_WIDTH - size - margin, WINDOW_HEIGHT - size - margin]

        self.menu_surf = pygame.Surface((size, size))
        self.menu_surf = self.menu_surf.convert_alpha()
        self.menu_surf.fill((0, 0, 0, 130))


    def display(self, index):
        self.menu_rect = self.menu_surf.get_rect()
        self.display_surface.blit(self.menu_surf, self.topleft, self.menu_rect)
        imagerect = self.menu_surfs[index].get_rect()

        position = (self.menu_rect.width / 2 - imagerect.width / 2, self.menu_rect.height / 2 - imagerect.height / 2)

        self.menu_surf.blit(self.menu_surfs[index], position, imagerect)



# class MenuItem(pygame.sprite.Sprite):
#     def __init__(self, rect, item):
#         pygame.sprite.Sprite.__init__(self)
#
#         self.item = item
#         self.image = pygame.Surface(rect.size)
#         self.rect = rect
#
#     def update(self):
#         self.image.fill(BACKGROUND)
#         rect = self.item.get_rect(center = (self.rect.width / 2, self.rect.height / 2))
#         self.image.blit(self.item, rect)