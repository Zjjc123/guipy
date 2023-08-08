import pygame
from guipy.components._component import Component
from guipy.utils import *


class Switch(Component):
    """
    Switch component
    """

    def __init__(self, width, height):
        """
        Switch init

        :param width: Width in pixels
        :param height: Height in pixels
        """
        self.width = width
        self.height = height

        self.off_surf = pygame.Surface((self.width, self.height)).convert_alpha()
        self.on_surf = pygame.Surface((self.width, self.height)).convert_alpha()

        self.state = False
        self.cb = None

        self._draw()

    def set_callback(self, cb):
        """
        Sets the function to run when the switch is changed

        :param cb: Callback function
        """
        self.cb = cb
        return self

    def _draw(self):
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

    def get_surf(self):
        """
        Gets the component's surface
        """
        if self.state:
            return self.on_surf
        else:
            return self.off_surf

    def update(self, rel_mouse, events):
        """
        Update the switch

        :param rel_mouse: Relative mouse position
        :param events: Pygame Event list
        """
        on_click = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                on_click = True

        if on_click and self._collide(rel_mouse):
            self.state = not self.state

            if self.cb != None:
                self.cb(self)
