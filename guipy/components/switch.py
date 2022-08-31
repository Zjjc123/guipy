import pygame
from guipy.components._component import Component
from guipy.utils import *


class Switch(Component):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.off_surf = self.root.copy()
        self.on_surf = self.root.copy()

        self.state = False
        self.prev_mouse_down = False
        self.root = self.off_surf

        self._render()

    def get_val(self):
        return self.state

    def set_funcs(self, on_func=None, off_func=None):
        self.on_func = on_func
        self.off_func = off_func
        return self

    def _render(self):
        spacer = 3
        corner = 7
        alpha = 200

        self.off_surf.fill(TRANSPARENT)
        surf = self.off_surf
        pygame.draw.rect(surf, (255, 0, 0, alpha), surf.get_rect(), 0, corner)
        pygame.draw.rect(surf, BLACK, surf.get_rect(), 1, corner)
        rect = pygame.Rect(
            spacer, spacer, self.width // 2 - spacer, self.height - spacer * 2
        )
        pygame.draw.rect(surf, GREY, rect, 0, corner)
        pygame.draw.rect(surf, BLACK, rect, 1, corner)

        self.on_surf.fill(TRANSPARENT)
        surf = self.on_surf
        pygame.draw.rect(surf, (0, 255, 0, alpha), surf.get_rect(), 0, corner)
        pygame.draw.rect(surf, BLACK, surf.get_rect(), 1, corner)
        rect = pygame.Rect(
            self.width // 2, spacer, self.width // 2 - spacer, self.height - spacer * 2
        )
        pygame.draw.rect(surf, GREY, rect, 0, corner)
        pygame.draw.rect(surf, BLACK, rect, 1, corner)

    def draw(self):
        if self.state:
            self.root = self.on_surf
        else:
            self.root = self.off_surf

    def update(self, rel_mouse, events):
        """
        Update the button

        :param rel_mouse: Relative mouse position
        :param events: Pygame Event list
        """

        mouse_down = pygame.mouse.get_pressed()[0]

        in_comp = self.root.get_rect().collidepoint(rel_mouse)
        on_click = mouse_down and not self.prev_mouse_down

        if on_click and in_comp:
            self.state = not self.state

            if self.state:
                if self.on_func != None:
                    self.on_func()
            else:
                if self.off_func != None:
                    self.off_func()

        self.prev_mouse_down = mouse_down
