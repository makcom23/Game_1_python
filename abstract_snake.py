from abc import ABC, abstractmethod
import pygame

class AbstractSnake(ABC):

    def __init__(self, surface, settings, window_width, window_height):
        self.surface = surface
        self.radius = 10
        self.settings = settings
        self.window_width = window_width
        self.window_height = window_height
        self.tail_count = 0
        self.crunch_sound = pygame.mixer.Sound ( "apple_crunch.wav" )
        self.lose_sound = pygame.mixer.Sound ( "lose.wav" )
        self.game_over_sound = pygame.mixer.Sound ( "game_over.wav" )


    @abstractmethod
    def show(self):
        pass

    def create(self, x, y):
        self.x = x
        self.y = y
        self.pos =(self.x, self.y)
        self.vizible = True

    def check_borders(self):
        if self.y <= 40:
            self.y = self.window_height-10
        elif self.y >= self.window_height:
            self.y = 50
        elif self.x <= 0:
            self.x = self.window_width-10
        elif self.x >= self.window_width:
            self.x = 10

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def game_over(self):
        pass

    def tail_show(self):
        pass