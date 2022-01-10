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
        self.__x = 0
        self.__y = 0
        self.__tick = 100

    def run(self):
        """"""
        while self.__isRunning:
            self.__event()
            self.__controls()
            self.launched()
            self.__display.show_screen(self.__platform.getPlatform(), self.__platform.getLastPlatform())
            self.isClicked()
            pygame.display.flip()


    def __event(self):
        """"""
        self.__gameClock.tick(self.__tick)
        self.__IsKeyDown = not len(self.__Touches) == 0 
        for event in pygame.event.get():
            if event.type == QUIT: self.__isRunning=False; pygame.quit(); sys.exit()
            elif event.type == KEYDOWN and event.key not in self.__Touches: self.__Touches.append(event.key)
            elif event.type == KEYUP and event.key in self.__Touches: self.__Touches.remove(event.key)
            elif event.type == MOUSEBUTTONDOWN and not self.__isClicked : self.__isClicked = True
            elif event.type == MOUSEBUTTONUP and self.__isClicked: self.__isClicked = False; self.__x, self.__y = -20,-20

    def __controls(self):
        """"""
        if not (self.__IsKeyDown):
            if self.__Touches==[K_SPACE]: 
                self.__isLaunched = not self.__isLaunched
            if not self.__isLaunched:
                if self.__Touches==[K_RIGHT]:
                    self.__platform.modifyPlatform()
                elif self.__Touches==[K_LEFT]:
                    self.__platform.previousPlatform()

    def launched(self):
        if self.__isLaunched:
            self.__platform.modifyPlatform()
            self.__tick = 100
        else: self.__tick = 1000

    def mouse_pos_is_okay(self,x,y):
        if y > 100:
            l,c = pygame.mouse.get_pos()
            c,l = c//self.__platform.getCaseSize(),  (l-100)//self.__platform.getCaseSize()
            if x != c or y != l:
                self.invert_case(l,c)
        return c,l
                 
    def invert_case(self, l,c):
        try:
            self.__platform.allPlatform.append(self.__platform.CopyPlatform(self.__platform.getPlatform()))
            if self.__platform.getPlatform()[l][c] == 0: 
                self.__platform.getPlatform()[l][c] = 1
            elif self.__platform.getPlatform()[l][c] ==1: 
                self.__platform.getPlatform()[l][c] = 0
        except: pass

    def isClicked(self):
        if self.__isClicked:
            x,y = pygame.mouse.get_pos()
            if y > 100:
                x,y = x//20, (y-100)//20
                if x != self.__x or y != self.__y:
                    self.invert_case(y,x)
                    self.__x, self.__y = x,y

g = Game(80,40)
g.run()