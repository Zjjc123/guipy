import sys
import os
import inspect

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.manager import GUIManager
from guipy.components.button import Button
from guipy.utils import *


def func(button):
    button.set_text(button.text + "!")
    print(button.text)


winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

man = GUIManager()
myButton1 = Button(width=200).set_callback(func)
myButton2 = Button(width=200).set_callback(func)
myButton3 = Button(width=200).set_callback(func)
myButton4 = Button(width=200).set_callback(func)

man.add(myButton1, (10, 25))
man.add(myButton2, (10, 75))
man.add(myButton3, (10, 125))
man.add(myButton4, (10, 175))
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    root.fill(WHITE)

    man.update(pygame.mouse.get_pos(), events)
    man.draw(root)
    pygame.display.update()
