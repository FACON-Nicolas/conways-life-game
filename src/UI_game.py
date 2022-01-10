import pygame
import pygame_gui

class UI:
    def __init__(self, width):
        pygame.init()
        self.manager = pygame_gui.UIManager((width,100))
        self.reset_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (200, 60)), text='Reset', manager=self.manager)
        self.last_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((240,20), (200, 60)), text="Last Step", manager=self.manager)
        self.next_step_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((460,20), (200, 60)), text="Next Step", manager=self.manager)
        self.pause_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((680,20), (200, 60)), text="Pause / Unpause", manager=self.manager)
        self.random_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((900,20), (200, 60)), text="Random", manager=self.manager)
