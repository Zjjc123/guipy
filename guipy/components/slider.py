import pygame
from guipy.components.component import Component


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
        self.root.fill((0, 0, 0, 0))

        p1 = (self.r, self.height // 2)
        p2 = (self.width - self.r, self.height // 2)

        pVal = (self.r + self.val * (self.width - self.r * 2), self.height // 2)

        pygame.draw.line(self.root, (57, 189, 248), p1, pVal, self.thickness)
        pygame.draw.line(self.root, (200, 200, 200), pVal, p2, self.thickness)

        pygame.draw.circle(self.root, (0, 0, 0), pVal, self.r)
        pygame.draw.circle(self.root, (255, 255, 255), pVal, self.r - 3)

    def update(self, rel_mouse, events):
        mouse_down = pygame.mouse.get_pressed()[0]

        # TODO put this in parent class
        in_comp = 0 <= rel_mouse[0] < self.width and 0 <= rel_mouse[1] < self.height
        on_click = mouse_down and not self.prev_mouse_down

        if in_comp and on_click:
            self.grabbed = True

        if not mouse_down:
            self.grabbed = False

        if self.grabbed:
            new_val = (rel_mouse[0] - self.r) / (self.width - 2 * self.r)

            if new_val < 0:
                new_val = 0
            elif new_val > 1:
                new_val = 1  # TODO add to parent class / helper classes/functions

            self.val = new_val

        self.prev_mouse_down = mouse_down
