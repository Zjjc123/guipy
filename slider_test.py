import sys
import pygame

from manager import GUIManager
from components.slider import Slider


pygame.init()

winW = 1000
winH = 1000

root = pygame.display.set_mode((winW, winH))

man = GUIManager()

mySlider = Slider(height=50, width=500, thickness=5, radius=12, initial_val=.4)
man.add(mySlider, (190, 190))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mySlider.val)

    root.fill((50, 50, 50))

    man.update()
    man.draw(root)
    pygame.display.update()
