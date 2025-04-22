# class apple
import pygame
import random as rnd

class Apple:
    def __init__(self, surface, color):
        self.x = rnd.randint(10,790)
        self.y = rnd.randint(10, 590)
        self.surface = surface
        self.color = color
        self.pos =(self.x, self.y)
        self.radius = 10
        self.color_tail = (30, 30, 30)

    def creating_apple(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, width=0)
        tail_end = (self.x, self.y - 15)
        pygame.draw.line(self.surface, self.color_tail, self.pos, tail_end, width=3)