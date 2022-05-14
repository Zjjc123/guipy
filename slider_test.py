import sys
import pygame
import colorsys

from manager import GUIManager
from components.slider import Slider


pygame.init()

winW = 1280
winH = 720

root = pygame.display.set_mode((winW, winH))

man = GUIManager()

mySlider = Slider(height=50, width=500, thickness=5, radius=12, initial_val=.4)
mySlider2 = Slider(height=50, width=500, thickness=5,
                   radius=12, initial_val=0)
mySlider3 = Slider(height=50, width=500, thickness=5,
                   radius=12, initial_val=.5)
mySlider4 = Slider(height=50, width=500, thickness=5,
                   radius=12, initial_val=.5)

man.add(mySlider, (0, 25))
man.add(mySlider2, (0, 75))
man.add(mySlider3, (0, 125))
man.add(mySlider4, (0, 175))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    root.fill((50, 50, 50))

    pygame.draw.circle(root, tuple(i * 255 for i in colorsys.hls_to_rgb(mySlider2.get_val(), mySlider3.get_val(), mySlider4.get_val())), (winW/2, winH/2),
                       10 + mySlider.get_val() * 100)

    man.update()
    man.draw(root)
    pygame.display.update()
