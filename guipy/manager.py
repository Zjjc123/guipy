class GUIManager:
    """
    GUI Manager

    Main class that is required for all UI components to work.
    Add components to the manager, update, and then render them all onto a surface
    """

    def __init__(self):
        """
        Initializes the GUIManager
        """
        self.components = []

    def add(self, component, pos):
        """
        Add component to the manager

        :param component: UI component to be added to the GUIManager
        :param pos: Position of UI component on screen

        """
        self.components.append((component, pos))

    def update(self, mouse_pos):
        """
        Update all components in the manager

        :param mouse_pos: Mouse position used to update the components so components understand the relative location
        :param events: pygame events used to update the components

        pos
            Position of UI on screen

        """
        for component in self.components:
            rel_mouse = tuple(i[0] - i[1] for i in zip(mouse_pos, component[1]))
            component[0].update(rel_mouse)

    def draw(self, root):
        """
        Render all components unto a surface

        :param root: the surface these components should be drawn on
        """
        for component in self.components:
            component[0].draw()
            root.blit(component[0].get_surf(), component[1])
