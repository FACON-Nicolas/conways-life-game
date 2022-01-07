import sys
import pygame
import GamePlatform
from pygame.locals import *
from display import Display

class Game:
    """"""
    def __init__(self, width, height):
        """"""
        self.__Touches = list()
        self.__isRunning = True
        self.__gameClock = pygame.time.Clock()
        self.__platform = GamePlatform.GamePlatform(height, width, 2, 3)
        self.__display = Display(self.__platform.getCaseSize()*self.__platform.getWidth(), 
            self.__platform.getCaseSize()*self.__platform.getHeight()) 

    def run(self):
        """"""
        while self.__isRunning:


    def event(self):
        """"""
        for e in pygame.event.get():
                if e == QUIT: self.__isRunning=False
                elif e==KEYDOWN and e.key not in self.__Touches: self.__Touches.append(e.key)
                elif e==KEYUP and e.key in self.__Touches: self.__Touches.append(e.key)
    
    def controls(self):
        """"""
        pass

        
g = Game(80,40)
g.run()