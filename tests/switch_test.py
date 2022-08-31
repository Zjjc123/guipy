import sys
import os
import inspect

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.manager import GUIManager
from guipy.components.switch import Switch
from guipy.utils import *


def func1():
    print("on")


def func2():
    print("off")


winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

man = GUIManager()
mySwitch1 = Switch(width=20, height=10).set_funcs(on_func=func1, off_func=func2)
mySwitch2 = Switch(width=30, height=15).set_funcs(on_func=func1, off_func=func2)
mySwitch3 = Switch(width=60, height=30).set_funcs(on_func=func1, off_func=func2)
mySwitch4 = Switch(width=200, height=300).set_funcs(on_func=func1, off_func=func2)

man.add(mySwitch1, (10, 25))
man.add(mySwitch2, (10, 75))
man.add(mySwitch3, (10, 125))
man.add(mySwitch4, (10, 175))
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    root.fill(WHITE)

    man.update(pygame.mouse.get_pos(), events)
    man.draw(root)
    pygame.display.update()
