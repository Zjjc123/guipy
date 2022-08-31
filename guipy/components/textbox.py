import pygame
from guipy.components._component import Component
from guipy.utils import *


class Textbox(Component):
    """
    Textbox component for text input
    """

    def __init__(self, width, font=None, default_text="Type here..."):
        """
        Textbox init

        :param width: Width of the textbox
        :param font: Pygame Font object to be used
        :param default_text: Text to be shown when textbox is empty
        """
        if font == None:
            self.font = get_default_font()
        else:
            self.font = font

        height = font.get_height() + 6
        super().__init__(width, height)

        self.active = False
        self.prev_mouse_down = False
        self.text = ""
        self.text_surf = font.render(default_text, True, (200, 200, 200))
        self.default = self.text_surf
        self.func = None

    def get_val(self):
        """
        Get current text
        """
        return self.text

    def set_func(self, func):
        """
        Set the function to be run when text is entered

        :param func: Function with signature (textbox:Textbox)
        """
        self.func = func
        return self

    def draw(self):
        """
        Renders the textbox
        """
        self.root.fill((0, 0, 0, 0))

        pygame.draw.rect(self.root, (255, 255, 255), self.root.get_rect())
        if self.active:
            pygame.draw.rect(self.root, (0, 0, 0), self.root.get_rect(), width=2)
        else:
            pygame.draw.rect(self.root, (0, 0, 0), self.root.get_rect(), width=1)
        self.root.blit(self.text_surf, (4, 3))

    def update(self, rel_mouse, events):
        """
        Update the textbox

        :param rel_mouse: Relative mouse position
        :param events: Pygame Event list (used to read keypresses)
        """

        mouse_down = pygame.mouse.get_pressed()[0]

        in_comp = self.root.get_rect().collidepoint(rel_mouse)
        on_click = mouse_down and not self.prev_mouse_down

        if on_click:
            if self.active and not in_comp and self.func != None:
                self.func(self)
            self.active = in_comp

        if self.active:

            for event in events:
                if event.type == pygame.KEYDOWN:
                    # check for backspace
                    if event.key == pygame.K_RETURN:
                        if self.func != None:
                            self.func(self)
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:  # add character
                        self.text += event.unicode

            if len(self.text) > 0:
                self.text_surf = self.font.render(self.text, True, (0, 0, 0))
            else:
                self.text_surf = self.default

        self.prev_mouse_down = mouse_down
