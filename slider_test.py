import pygame
import sys
from components.slider import Slider
from manager import GUIManager

pygame.init()

winW = 1000
winH = 1000

root = pygame.display.set_mode((winW, winH))

mySlider = Slider(50, 500, 10, 10, .4)

man = GUIManager()
man.add(mySlider, (190, 190))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mySlider.val)

    root.fill((100, 100, 100))

    man.update()
    man.draw(root)
    pygame.display.update()
