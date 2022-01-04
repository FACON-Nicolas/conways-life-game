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
        self.__sizeCase = 20

    def show_platform(self, platform: List[List[int]]):
        """"""
        gray, white, black = (127,127,127), (255,255,255), (0,0,0) 
        self.__surface.fill(gray)
        for raw in platform.__len__():
            for columns in platform[0].__len__():
                if (platform[raw][columns] == 0):
                    pygame.draw.rect(self.__surface, white, pygame.Rect(
                        columns*self.__sizeCase, raw*self.__sizeCase, 
                        self.__sizeCase-1, self.__sizeCase-1))

                elif (platform[raw][columns] == 1):
                    pygame.draw.rect(self.__surface, black, pygame.Rect(
                        columns*self.__sizeCase, raw*self.__sizeCase, 
                        self.__sizeCase-1, self.__sizeCase-1))   

    def getWidth(self):
        """"""
        return self.__WIDTH

    def getHeight(self):
        """"""
        return self.__HEIGHT

    def getSizeCase(self):
        """"""
        return self.__sizeCase