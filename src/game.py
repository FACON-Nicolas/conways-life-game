import sys
import pygame
from pygame import display
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
            if self.__isLaunched: self.launched()
            self.__display.show_screen(self.__platform.getPlatform())
            pygame.display.flip()

    def __event(self):
        """"""
        self.__gameClock.tick(60)
        self.__IsKeyDown = not len(self.__Touches) == 0 
        for event in pygame.event.get():
            if event.type == QUIT: self.__isRunning=False; pygame.quit(); sys.exit()
            elif event.type == KEYDOWN and event.key not in self.__Touches: self.__Touches.append(event.key)
            elif event.type == KEYUP and event.key in self.__Touches: self.__Touches.remove(event.key)
            elif event.type == MOUSEBUTTONDOWN and not self.__isClicked: self.__isClicked = True
            elif event.type == MOUSEBUTTONUP and self.__isClicked: self.__isClicked = False

    def __controls(self):
        """"""
        if not (self.__IsKeyDown):
            if self.__Touches==[K_SPACE]: 
                print('uhn')
                self.__isLaunched = not self.__isLaunched
            if not self.__isLaunched:
                if self.__Touches==[K_RIGHT]:
                    self.__platform.modifyPlatform()
                elif self.__Touches==[K_LEFT]:
                    self.__platform.previousPlatform()

    def launched(self):
        self.__platform.modifyPlatform()

g = Game(80,40)
g.run()