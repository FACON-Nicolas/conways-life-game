import pygame
from pygame.locals import *
from display import Display
import GamePlatform

class Game:
    """"""
    def __init__(self, width, height):
        """"""
        self.__platform = GamePlatform.GamePlatform(height, width, 2, 3)
        self.__display = Display(self.__platform.getCaseSize()*self.__platform.getHeight(), 
            self.__platform.getCaseSize()*self.__platform.getWidth()) 

    def run(self):
        """"""
        pass

    def event(self):
        """"""
        pass
    
    def controls(self):
        """"""
        pass

        
g = Game()
g.run()