# game time class
import pygame

class GameTime:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.start_ticks = pygame.time.get_ticks()

    def start(self):
        self.count = int((pygame.time.get_ticks() - self.start_ticks)/1000)
        self.minutes = int(self.count //60)
        self.seconds = self.count % 60

    def get_time(self):
        return (f'{self.minutes} min : {self.seconds} sec')