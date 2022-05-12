import pygame

class Slider:
    offset = 10
    
    def __init__(self, height, width, thickness = 2, radius=10, initial_val=0):
        self.height = height
        self.width = width
        self.thickness = thickness
        self.val = initial_val
        self.r = radius
        self.root = pygame.Surface((self.width, self.height))
    
    def get_surf(self):
        return self.root
        

    def update(self, rel_mouse):
        # mouse_pressed = pygame.mouse.get_pressed()
        # if mouse_pressed[0]:
        #     if something.collidepoint(rel_mouse):
        #         pass
            
        self.root.fill((255,255,255))
        
        p1 = (Slider.offset,self.height//2)
        p2 = (self.width-Slider.offset,self.height//2)
        
        # pVal = (self.r + self.val * (self.width - self.r*2), self.height//2)
        pVal=rel_mouse

        pygame.draw.line(self.root,(0,0,0),p1,p2,self.thickness)
        pygame.draw.circle(self.root,(0,0,0),pVal,self.r)
    
