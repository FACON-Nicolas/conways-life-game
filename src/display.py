import pygame
from typing import List

class Display: 
    """"""
    def __init__(self, width, height):
        """"""
        self.__WIDTH = width+1
        self.__HEIGHT = height+101
        self.__surface = pygame.display.set_mode((self.__WIDTH, self.__HEIGHT))
        self.__surface_name = pygame.display.set_caption('Life-game')
        self.__sizeCase = 20

    def show_screen(self, platform: List[List[int]], last_platform: List[List[int]]):
        """"""
        if platform != last_platform:
            gray, white, black = (127,127,127), (255,255,255), (0,0,0) 
            pygame.draw.rect(self.__surface, white, (0,0,self.getWidth(), 100))
            for raw in range(platform.__len__()):
                for columns in range(platform[0].__len__()):
                    if platform[raw][columns] != last_platform[raw][columns]:
                        if (platform[raw][columns] == 0):
                            pygame.draw.rect(self.__surface, white, pygame.Rect(
                                columns*self.__sizeCase+1, raw*self.__sizeCase+101, 
                                self.__sizeCase-1, self.__sizeCase-1))

                        elif (platform[raw][columns] == 1):
                            pygame.draw.rect(self.__surface, black, pygame.Rect(
                                columns*self.__sizeCase+1, raw*self.__sizeCase+101, 
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

    def getSurface(self):
        return self.__surface