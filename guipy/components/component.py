import pygame


class Component:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = pygame.Surface((width, height)).convert_alpha()

    def get_surf(self):
        return self.root

    def draw(self):
        pass

    def update(self, rel_mouse, events):
        pass
