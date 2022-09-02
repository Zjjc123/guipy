import sys
import os
import inspect
import time

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.manager import GUIManager
from guipy.components.plot import LivePlot
from guipy.utils import *

winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

myPlot1 = LivePlot(height=winH, width=winW)

man = GUIManager()
man.add(myPlot1, (0, 0))


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

    root.fill(LIGHT_GREY)

    p = pygame.mouse.get_pos()

    myPlot1.add([(time.time(), p[1])])

    man.update(p, [])
    man.draw(root)

    pygame.display.update()
