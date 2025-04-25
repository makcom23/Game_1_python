# class apple
import pygame
import random as rnd

class Apple:
    def __init__(self, surface, cell_size, window_width, window_height):
        self.vizible = False
        self.surface = surface
        self.radius = 10
        self.color_tail = (30, 30, 30)
        self.COLOR_APPLE = (200, 30, 30)
        self.cell_size = cell_size
        self.half_cell = 10
        self.window_width = window_width
        self.window_height = window_height

    def drawing_apple(self):
        if self.vizible:
            pygame.draw.circle(self.surface, self.COLOR_APPLE, self.pos, self.radius, width=0)
            tail_end = (self.x, self.y - 15)
            pygame.draw.line(self.surface, self.color_tail, self.pos, tail_end, width=3)

    def creating_new_apple(self):
        self.x = rnd.randint(1, (self.window_width - 20)//self.cell_size) * self.cell_size + self.half_cell
        self.y = rnd.randint(1, (self.window_height - 20)//self.cell_size) * self.cell_size + self.half_cell
        self.pos =(self.x, self.y)
        self.vizible = True
