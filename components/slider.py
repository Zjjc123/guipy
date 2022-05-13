import pygame


class Slider:
    def __init__(self, height, width, thickness=2, radius=10, initial_val=0):
        self.height = height
        self.width = width
        self.thickness = thickness
        self.val = initial_val
        self.r = radius
        self.root = pygame.Surface((self.width, self.height))
        
        self.grabbed = False
        self.prev_mouse_down = False

        self.draw()

    def get_surf(self):
        return self.root
    
    def get_val(self):
        return self.val

    def draw(self):
        self.root.fill((255, 255, 255))

        p1 = (self.r, self.height//2)
        p2 = (self.width-self.r, self.height//2)

        pVal = (self.r + self.val * (self.width - self.r*2), self.height//2)

        pygame.draw.line(self.root, (0, 0, 0), p1, p2, self.thickness)
        pygame.draw.circle(self.root, (0, 0, 0), pVal, self.r)


    def update(self, rel_mouse):
        mouse_down = pygame.mouse.get_pressed()[0]

        in_comp = (0 <= rel_mouse[0] < self.width and 0 <= rel_mouse[1] < self.height) # TODO put this in parent class
        on_click = (mouse_down and not self.prev_mouse_down)
        
        if (in_comp and on_click):
            self.grabbed = True

        if (not mouse_down):
            self.grabbed = False
 
        if self.grabbed:
            new_val = (rel_mouse[0]-self.r)/(self.width-2*self.r)
            
            if new_val < 0: new_val = 0
            elif new_val > 1: new_val = 1 # TODO add to parent class / helper classes/functions

            self.val = new_val
            self.draw()

        self.prev_mouse_down = mouse_down
