import pygame

from guipy.components.component import Component

class Textbox(Component):
    def __init__(self, width, height, font=None, default_text='Type here...'):
        height = font.get_height()+6
        super().__init__(width, height)

        self.active = False
        self.prev_mouse_down = False
        self.text = ''
        self.font = font
        self.text_surf = font.render(default_text,True,(200,200,200))
        self.default = self.text_surf
        

    def get_val(self):
        return self.text

    def draw(self):
        
        self.root.fill((0, 0, 0, 0))

        pygame.draw.rect(self.root,(255,255,255),self.root.get_rect())
        if self.active: pygame.draw.rect(self.root,(0,0,0),self.root.get_rect(),width=2)
        else: pygame.draw.rect(self.root,(0,0,0),self.root.get_rect(),width=1)
        self.root.blit(self.text_surf,(4,3))

    def update(self, rel_mouse, events):
        mouse_down = pygame.mouse.get_pressed()[0]

        in_comp = self.root.get_rect().collidepoint(rel_mouse)
        on_click = mouse_down and not self.prev_mouse_down

        if on_click:
            self.active = in_comp
        
        if self.active:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    # check for backspace
                    if event.key == pygame.K_RETURN:
                        self.active = False
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else: # add character
                        self.text += event.unicode

            if len(self.text) > 0:
                self.text_surf = self.font.render(self.text,True,(0,0,0))
            else:
                self.text_surf = self.default
            
        self.prev_mouse_down = mouse_down