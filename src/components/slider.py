import pygame
from component import Component


class Slider(Component):
    def __init__(self, width, height, thickness=2, radius=10, initial_val=0):
        super().__init__(width, height)

        self.thickness = thickness
        self.val = initial_val
        self.r = radius

        self.grabbed = False
        self.prev_mouse_down = False

    def get_val(self):
        return self.val

    def draw(self):
        self.root = self.root.convert_alpha()
        self.root.fill((0, 0, 0, 0))

        p1 = (self.r, self.height//2)
        p2 = (self.width-self.r, self.height//2)

        pVal = (self.r + self.val * (self.width - self.r*2), self.height//2)

        pygame.draw.line(self.root, (57, 189, 248), p1, pVal, self.thickness)
        pygame.draw.line(self.root, (200, 200, 200), pVal, p2, self.thickness)

        pygame.draw.circle(self.root, (0, 0, 0), pVal, self.r)
        pygame.draw.circle(self.root, (255, 255, 255), pVal, self.r - 3)

    def update(self, rel_mouse):
        mouse_down = pygame.mouse.get_pressed()[0]

        # TODO put this in parent class
        in_comp = (0 <= rel_mouse[0] < self.width and 0 <=
                   rel_mouse[1] < self.height)
        on_click = (mouse_down and not self.prev_mouse_down)

        if (in_comp and on_click):
            self.grabbed = True

        if (not mouse_down):
            self.grabbed = False

        if self.grabbed:
            new_val = (rel_mouse[0]-self.r)/(self.width-2*self.r)

            if new_val < 0:
                new_val = 0
            elif new_val > 1:
                new_val = 1  # TODO add to parent class / helper classes/functions

            self.val = new_val

        self.prev_mouse_down = mouse_down


if __name__ == "__main__":
    import sys
    from slider import Slider
    import colorsys

    import os
    import inspect

    currentdir = os.path.dirname(os.path.abspath(
        inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)

    from manager import GUIManager

    pygame.init()

    winW = 1280
    winH = 720

    root = pygame.display.set_mode((winW, winH))

    man = GUIManager()

    mySlider = Slider(height=50, width=500, thickness=5,
                      radius=12, initial_val=.4)
    mySlider2 = Slider(height=50, width=500, thickness=5,
                       radius=12, initial_val=0)
    mySlider3 = Slider(height=50, width=500, thickness=5,
                       radius=12, initial_val=.5)
    mySlider4 = Slider(height=50, width=500, thickness=5,
                       radius=12, initial_val=.5)

    man.add(mySlider, (0, 25))
    man.add(mySlider2, (0, 75))
    man.add(mySlider3, (0, 125))
    man.add(mySlider4, (0, 175))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        root.fill((50, 50, 50))

        color = tuple(i * 255 for i in colorsys.hls_to_rgb(mySlider2.get_val(),
                      mySlider3.get_val(), mySlider4.get_val()))

        pygame.draw.circle(root, color, (winW/2, winH/2),
                           10 + mySlider.get_val() * 100)

        man.draw(root)
        man.update()
        pygame.display.update()
