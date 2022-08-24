class GUIManager:
    """
    Guipy GUI Manager
    """

    def __init__(self):
        """
        Initialize GUIManager
        """
        self.components = []

    def add(self, component, pos):
        """
        Add component to manager

        :param component: UI component to be added to the GUIManager
        :param pos: Position of UI on screen

        """
        self.components.append((component, pos))

    def update(self, mouse_pos):
        """
        Add component to manager

        Parameters
        ----------
        component
            UI componenet to be added

        pos
            Position of UI on screen

        """
        for component in self.components:
            rel_mouse = tuple(i[0]-i[1] for i in zip(mouse_pos, component[1]))
            component[0].update(rel_mouse)

    def draw(self, root):
        for component in self.components:
            component[0].draw()
            root.blit(component[0].get_surf(), component[1])
