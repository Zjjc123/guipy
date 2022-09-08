import pygame


class Component:
    def __init__(self, width, height):
        """
        Component init. Should create a surface for the component
        """
        self.width = width
        self.height = height
        self.root = pygame.Surface((width, height))

    def _draw(self):
        """
        All the drawing
        """

    def render(self):
        """
        Makes sure the root is ready to be used.

        :return: Surface
        """
        self._draw()
        return self.root

    def update(self, rel_mouse, events):
        """
        Update the component. Should not draw anything, just change state.

        :param rel_mouse: Mouse position relative to the component
        :param events: Pygame event list
        """

    def _collide(self, rel_mouse):
        return 0 <= rel_mouse[0] < self.width and 0 <= rel_mouse[1] < self.height
