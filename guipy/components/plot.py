import pygame
from guipy.components._component import Component
from guipy.utils import *
import math


def line(surf, points):
    """
    Example/default plot style
    :param surf: Surface to draw to
    :param points: List of pixel coordinates to draw. ex: [(1,1),(2,3),...]
    """
    last = None
    for p in points:
        if last:
            pygame.draw.line(surf, BLUE, last, p, 2)
        last = p


class Plot(Component):
    """
    Plot component. Simple and fast way to display data
    """

    def __init__(self, width, height, xlabel=None, ylabel=None):
        """
        Plot init

        :param width: Plot width in pixels
        :param height: Plot height in pixels
        :param xlabel: X-axis label
        :param ylabel: Y-axis label
        """
        super().__init__(width, height)

        self.xlabel = xlabel
        self.ylabel = ylabel

        self.xaxis_spacer = 100
        self.yaxis_spacer = 100

        self.xmin = 0
        self.xmax = 1
        self.ymin = 0
        self.ymax = 1
        self.points = []

        self.font = get_default_font()

        self.window = pygame.Surface(
            (width - self.yaxis_spacer, height - self.xaxis_spacer)
        )
        self._windrect = self.window.get_rect().inflate(-5, -5)

        self.clear()

    def _x(self, x):  # coordinate to pixel
        return translate(
            x, self.xmin, self.xmax, self._windrect.left, self._windrect.right
        )

    def _y(self, y):  # coordinate to pixel
        return translate(
            y, self.ymax, self.ymin, self._windrect.top, self._windrect.bottom
        )

    def _render(self):
        w = self.window.get_width()
        h = self.window.get_height()

        self.root.fill((0, 0, 0, 0))

        # draw x-axis
        scale = math.floor(math.log10(self.xmax - self.xmin)) - 1
        res = 10**scale

        i = math.ceil(self.xmin / res) * res

        while i <= self.xmax:
            p1 = (self._x(i), h)

            if round(i / res) % 10 == 0:
                p2 = (p1[0], h + self.xaxis_spacer / 4)
                n = str(i) if scale < -1 else str(int(i))
                num = self.font.render(n, True, BLACK)
                self.root.blit(num, p2)
            else:
                p2 = (p1[0], h + self.xaxis_spacer / 8)
            pygame.draw.line(self.root, BLACK, p1, p2, 1)
            i = round(i + res, -scale)

        if self.xlabel:
            label = self.font.render(self.xlabel, True, BLACK)
            p = ((w - label.get_width()) / 2, self.height - label.get_height())
            self.root.blit(label, p)

        # draw y-axis
        scale = math.floor(math.log10(self.ymax - self.ymin)) - 1
        res = 10**scale

        i = math.ceil(self.ymin / res) * res

        while i <= self.ymax:
            p1 = (w, self._y(i))

            if round(i / res) % 10 == 0:
                p2 = (w + self.yaxis_spacer / 4, p1[1])
                n = str(i) if scale < -1 else str(int(i))
                self.root.blit(self.font.render(n, True, BLACK), p2)
            else:
                p2 = (w + self.yaxis_spacer / 8, p1[1])
            pygame.draw.line(self.root, BLACK, p1, p2, 1)
            i = round(i + res, -scale)

        if self.ylabel:
            label = self.font.render(self.ylabel, True, BLACK)
            label = pygame.transform.rotate(label, 90)
            p = (self.width - label.get_width(), (h - label.get_height()) / 2)
            self.root.blit(label, p)

    def set_range(self, xrange, yrange):
        """
        Sets the plot X and Y range and draws the axes using the new range.

        :param xrange: List of minimum and maximum X values. ex: (0,100)
        :param yrange: List of minimum and maximum Y values. ex: (0,100)
        """
        self.xmin = xrange[0]
        self.xmax = xrange[1]
        self.ymin = yrange[0]
        self.ymax = yrange[1]

        self._render()

    def plot(self, data, style=line):
        """
        Plots a list of points

        :param data: List of points to be plotted. ex: [(1.0,1.0),(1.2,1.3),...]
        :param style: Style function to be used. Should have the signature (surf:Surface, points:List[Tuple])
        """
        self.points = list((self._x(d[0]), self._y(d[1])) for d in data)
        style(self.window, self.points)
        return self.points

    def clear(self):
        """
        Clears the window
        """
        self.window.fill(WHITE)

    def draw(self):
        """
        Draws the window onto the plot
        """
        self.root.blit(self.window, (0, 0))
        pygame.draw.rect(self.root, BLACK, self.window.get_rect(), 1)
