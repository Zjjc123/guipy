import pygame
from guipy.components._component import Component
from guipy.utils import *


class Button(Component):
    """
    Button component
    """

    def __init__(self, width=None, height=None, font=None, text="Bruh", func=None):
        """
        Button init

        :param width: button width in pixels, defaults to fit text
        :param height: button height in pixels, defaults to fit text
        :param font: pygame Font object to use
        :param text: text to display on the button
        :param func: function to run when button is released
        """
        if font == None:
            self.font = get_default_font()
        else:
            self.font = font

        min_w, min_h = self.font.size(text)
        if width == None:
            width = min_w + 6
        if height == None:
            height = min_h
        super().__init__(width, height)

        self.pressed = False
        self.prev_mouse_down = False

        self.set_text(text)
        self.set_func(func)

    def get_val(self):
        """
        Get current state
        """
        return self.pressed

    def set_func(self, func):
        """
        Set the function to be run when button is released

        :param func: Function with signature (button:Button)
        """
        self.func = func
        return self

    def set_text(self, text):
        """
        Sets the text on the button and redraws the surface

        :param text:
        """
        self.text = text
        text_surf = self.font.render(text, True, BLACK)

        x, y = sub_vector(self.root.get_size(), text_surf.get_size())
        pos = (x // 2, y // 2)

        surf = self.root.copy()
        pygame.draw.rect(surf, LIGHT_GREY, surf.get_rect())
        pygame.draw.rect(surf, DARK_GREY, surf.get_rect(), 1)
        surf.blit(text_surf, pos)
        self.off_surf = surf

        surf = self.root.copy()
        pygame.draw.rect(surf, GREY, surf.get_rect())
        pygame.draw.rect(surf, DARK_GREY, surf.get_rect(), 1)
        surf.blit(text_surf, pos)
        self.on_surf = surf

        return self

    def draw(self):
        """
        Renders the button
        """
        self.root.fill((0, 0, 0, 0))

        if self.pressed:
            self.root.blit(self.on_surf, (0, 0))
        else:
            self.root.blit(self.off_surf, (0, 0))

    def update(self, rel_mouse, events):
        """
        Update the button

        :param rel_mouse: Relative mouse position
        :param events: Pygame Event list
        """

        mouse_down = pygame.mouse.get_pressed()[0]

        in_comp = self.root.get_rect().collidepoint(rel_mouse)
        on_release = not mouse_down and self.prev_mouse_down

        if self.pressed and on_release:
            self.pressed = False
            if self.func != None:
                self.func(self)

        if mouse_down and in_comp:
            self.pressed = True

        self.prev_mouse_down = mouse_down
