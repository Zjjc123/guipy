import pygame


class GUIManager:
    def __init__(self):
        self.components = []

    def add(self, component, pos):
        self.components.append((component, pos))

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for component in self.components:
            rel_mouse = tuple(i[0]-i[1] for i in zip(mouse_pos, component[1]))
            component[0].update(rel_mouse)

    def draw(self, root):
        for component in self.components:
            component[0].draw()
            root.blit(component[0].get_surf(), component[1])
