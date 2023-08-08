import pygame
from guipy.components._component import Component
from guipy.utils import *


class Text(Component):
    """
    Text component for displaying text
    """

    def __init__(self, font=None, default_text="Your text here!", color=BLACK):
        """
        Text init

        :param font: Pygame Font object to be used
        :param default_text: Text to be shown
        """
        if font == None:
            self.font = get_default_font()
        else:
            self.font = font

        self.set_text(default_text, color)
        self.func = None

    def set_func(self, func):
        """
        Set the callback to be run when the text is selected

        :param cb: Callback function
        """
        self.func = func
        return self
    
    def set_text(self, text, color=None):
        if color: self.color = color
        self.text = text
        self._draw()
        self.width = self.root.get_width()
        self.height = self.root.get_height()

    def _draw(self):
        """
        Draws the textbox
        """
        self.root = self.font.render(self.text, True, self.color)
        
    def update(self, rel_mouse, events):
        """
        Update the textbox

        :param rel_mouse: Relative mouse position
        :param events: Pygame Event list (used to read keypresses)
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self._collide(rel_mouse)):
                    self.func(self)
