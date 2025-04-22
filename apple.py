# class apple
import pygame
import random as rnd

class Apple:
    def __init__(self, surface):
        self.vizible = False
        self.surface = surface
        self.radius = 10
        self.color_tail = (30, 30, 30)
        self.COLOR_APPLE = (200, 30, 30)

    def drawing_apple(self):
        if self.vizible:
            pygame.draw.circle(self.surface, self.COLOR_APPLE, self.pos, self.radius, width=0)
            tail_end = (self.x, self.y - 15)
            pygame.draw.line(self.surface, self.color_tail, self.pos, tail_end, width=3)

    def creating_new_apple(self):
        self.x = rnd.randint(10,790)
        self.y = rnd.randint(10, 590)
        self.pos =(self.x, self.y)
        self.vizible = True
