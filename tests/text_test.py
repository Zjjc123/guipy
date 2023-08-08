import sys
import os
import inspect

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.manager import GUIManager
from guipy.components.text import Text


def f(x):
    print(x.text)
    x.set_text(x.text + " beep")


font1 = pygame.font.SysFont("Microsoft Sans Serif", 20)
font2 = pygame.font.SysFont("Comic Sans MS", 20)
font3 = pygame.font.SysFont("consolas", 20)
font4 = pygame.font.SysFont("arial", 20)

winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

man = GUIManager()
myText1 = Text(font1, default_text="I'm text!").set_func(f)
myText2 = Text(font2, default_text="I'm a label.").set_func(f)
myText3 = Text(font3, default_text="I'm a caption,").set_func(f)
myText4 = Text(font4, default_text="I'm a paragraph?").set_func(f)

man.add(myText1, (10, 25))
man.add(myText2, (400, 100))
man.add(myText3, (10, 125))
man.add(myText4, (300, 300))
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    root.fill((200, 200, 200))

    man.update(pygame.mouse.get_pos(), events, root)
    pygame.display.update()
