import pygame
from typing import List
from random import randint

class GamePlatform:
    """"""
    def __init__(self, height, width, min, max):
        self.__MAX_HEIGHT = 40
        self.__MAX_WIDTH = 80
        self.__MIN_SIZE = 10
        self.__HEIGHT = self.__SizeIsCorrect(height, self.__MAX_HEIGHT)
        self.__WIDTH = self.__SizeIsCorrect(width, self.__MAX_WIDTH)
        self.__MIN = min
        self.__MAX = max 
        self.__sizeCase = 20
        self.__state = 0
        self.platform = self.makePlatform(self.__WIDTH, self.__HEIGHT)
        self.allPlatform = []

    def isRange(self, case):
        l,c = case
        return l in range(self.platform.__len__()) and c in range(self.platform[0].__len__())

    def __SizeIsCorrect(self, size, max):
        assert(size >= self.__MIN_SIZE)
        if size in range(self.__MIN_SIZE, max): return size
        return max

    def CopyPlatform(self, platform=[]):
        """"""
        return [i.copy() for i in self.platform] if platform == [] else [i.copy() for i in platform]

    def makePlatform(self, w, h, v=0):
        """"""
        return [[v for i in range(w)]for j in range(h)]

    def checkCase(self, pos: tuple, platform: List[List[int]]):
        """"""
        cases = 0
        r,c = pos
        for r_dir in range(-1,2):
            for c_dir in range(-1,2):
                if (r_dir, c_dir) != (0,0):
                    if self.isRange((r+r_dir, c+c_dir)):
                        if platform[r+r_dir][c+c_dir]:
                            cases += 1
        return cases

    def modifyPlatform(self,  platform=[]):
        """"""
        if platform==[]: platform=self.platform
        copy = self.CopyPlatform()
        self.allPlatform.append(copy)
        for r in range(platform.__len__()):
            for c in range(platform[0].__len__()):
                cases = self.checkCase((r,c), copy)
                if cases in range(self.__MIN,self.__MAX+1):
                    if cases == 3: 
                        platform[r][c] = 1
                else: platform[r][c] = 0

    def previousPlatform(self):
        """"""
        if self.allPlatform.__len__() > 0:
            self.platform = self.CopyPlatform(self.allPlatform.pop())

    def getCaseSize(self):
        """"""
        return self.__sizeCase

    def getWidth(self):
        """"""
        return self.__WIDTH

    def getHeight(self):
        """"""
        return self.__HEIGHT

    def getPlatform(self):
        """"""
        return self.platform

    def getLastPlatform(self):
        """"""
        return self.CopyPlatform(self.allPlatform[len(self.allPlatform)-1]) \
        if len(self.allPlatform) > 0 else self.makePlatform(self.getWidth(), self.getHeight(), 1)

    def randomPlatform(self,w,h):
        self.allPlatform.append(self.CopyPlatform(self.platform))
        self.platform =  self.CopyPlatform([[randint(0,1) for i in range(w)]for j in range(h)])