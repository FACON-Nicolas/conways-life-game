import pygame
from typing import List

class Display: 
    """"""
    def __init__(self, width, height):
        """"""
        self.__WIDTH = width
        self.__HEIGHT = height
        self.__surface = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__surface_name = pygame.display.set_caption('Day-Life')

    def show_platform(self, platform: List[List[int]]):
        """"""
        gray, white, black = (127,127,127), (255,255,255), (0,0,0) 
        self.__surface.fill(gray)
        for raw in platform.__len__():
            for columns in platform[0].__len__():
                if (platform[raw][columns] == 0):
                    pygame.draw.rect(self.__surface, white, pygame.Rect(columns*30, raw*30, 29, 29))
                elif (platform[raw][columns] == 1):
                    pygame.draw.rect(self.__surface, black, pygame.Rect(columns*30, raw*30, 29, 29))       