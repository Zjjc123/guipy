import sys
import os
import inspect

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.manager import GUIManager
from guipy.components.textbox import Textbox

pygame.init()
pygame.font.init()

myFont = pygame.font.SysFont("Microsoft Sans Serif", 20)

winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

man = GUIManager()
myTextbox1 = Textbox(width=400, font=myFont)
myTextbox2 = Textbox(width=400, font=myFont)
myTextbox3 = Textbox(width=400, font=myFont)
myTextbox4 = Textbox(width=400, font=myFont)

man.add(myTextbox1, (10, 25))
man.add(myTextbox2, (10, 75))
man.add(myTextbox3, (10, 125))
man.add(myTextbox4, (10, 175))
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    root.fill((200, 200, 200))
    man.draw(root)
    man.update(pygame.mouse.get_pos(), events)
    pygame.display.update()
