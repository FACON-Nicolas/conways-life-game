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
        self.__isClicked = False
        self.__IsKeyDown = False
        self.__isLaunched = False
        self.__gameClock = pygame.time.Clock()
        self.__platform = GamePlatform.GamePlatform(height, width, 2, 3)
        self.__display = Display(self.__platform.getCaseSize()*self.__platform.getWidth(), 
            self.__platform.getCaseSize()*self.__platform.getHeight()) 

    def run(self):
        """"""
        while self.__isRunning:
            self.__event()
            self.__controls()
            self.__display.show_platform(self.__platform.getPlatform())
            pygame.display.flip()

    def __event(self):
        """"""
        self.__IsKeyDown = len(self.__Touches) == 0 
        self.__gameClock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT: self.__isRunning=False; pygame.quit(); sys.exit()
            elif event.type == KEYDOWN and event.key not in self.__Touches: self.__Touches.append(event.key)
            elif event.type == KEYUP and event.key in self.__Touches: self.__Touches.remove(event.key)
            elif event.type == MOUSEBUTTONDOWN and not self.__isClicked: self.__isClicked = True
            elif event.type == MOUSEBUTTONUP and self.__isClicked: self.__isClicked = False

    def __controls(self):
        """"""
        if not (self.__IsKeyDown):
            if not self.__isLaunched:
                if self.__Touches==[K_SPACE]:pass
                elif self.__Touches==[K_RIGHT]:pass
            elif self.__Touches==[K_ESCAPE]:pass

g = Game(80,40)
g.run()