import pygame
from pygame.locals import *
from display import Display
from Platform import GamePlatform

class Game:
    """"""
    def __init__(self, width, height):
        """"""
        self.__platform = GamePlatform() 