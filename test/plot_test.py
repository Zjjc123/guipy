import sys
import os
import inspect

import pygame

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from guipy.manager import GUIManager
from guipy.components.plot import Plot

pygame.init()

winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

myPlot1 = Plot(height=winH, width=winW, xlabel="X axis", ylabel="Y axis")

man = GUIManager()
man.add(myPlot1, (0, 0))

x = 1
y = 1

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
    root.fill((200, 200, 200))

    p = pygame.mouse.get_pos()
    x = p[0] if p[0] else x
    y = p[1] if p[1] else y

    myPlot1.set_range((0, x), (0, y))

    myPlot1.clear()
    myPlot1.plot(
        [(5, 35), (0, 40), (0, 60), (10, 70), (20, 60), (20, 40), (10, 30), (10, 10)]
    )
    myPlot1.plot(
        [(10, 60), (10, 40), (0, 30), (0, 10), (10, 0), (20, 10), (20, 30), (15, 35)]
    )

    man.draw(root)
    # man.update(pygame.mouse.get_pos(),events)
    pygame.display.update()
