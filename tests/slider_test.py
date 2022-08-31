import os
import sys
import inspect
import colorsys

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.components.slider import Slider
from guipy.manager import GUIManager
from guipy.utils import *

winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

man = GUIManager()

mySlider = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0.4)
mySlider2 = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0)
mySlider3 = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0.5)
mySlider4 = Slider(height=50, width=500, thickness=5, radius=12, initial_val=0.5)

man.add(mySlider, (0, 25))
man.add(mySlider2, (0, 75))
man.add(mySlider3, (0, 125))
man.add(mySlider4, (0, 175))

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    root.fill((50, 50, 50))

    color = tuple(
        i * 255
        for i in colorsys.hls_to_rgb(
            mySlider2.get_val(), mySlider3.get_val(), mySlider4.get_val()
        )
    )
    center = (winW // 2, winH // 2)
    r = 10 + mySlider.get_val() * 100
    pygame.draw.circle(root, color, center, r)
    pygame.draw.circle(root, BLACK, center, r, 3)

    man.draw(root)
    man.update(pygame.mouse.get_pos(), events)
    pygame.display.update()
