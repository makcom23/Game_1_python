import pygame
import random as rnd

class Snake:
    def __init__(self, surface, colors, cell_size, window_width, window_height):
        self.vizible = False
        self.surface = surface
        self.radius = 10
        self.eye = 2
        self.COLOR_EYE = colors['COLOR_EYE']
        self.COLOR_SNAKE = colors['COLOR_SNAKE']
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        self.window_width = window_width
        self.window_height = window_height

    def snake_head(self):
        pygame.draw.circle(self.surface, self.COLOR_SNAKE, self.pos, self.radius, width=0) # snake's head
        pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x-3, self.y-3), self.eye, width=0) # snake's left eye
        pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x+3, self.y-3), self.eye, width=0) # snake's right eye
        pygame.draw.line(self.surface, self.COLOR_EYE, (self.x-3, self.y+6), (self.x+3, self.y+6), width=2) # snake's mouth

    def snake_tail_add(self):
        pygame.draw.circle(self.surface, self.COLOR_SNAKE, self.pos, self.radius, width=0) # snake's tail
        
    def snake_head_pos(self):
        self.x = rnd.randint(1, (self.window_width - 20)//self.cell_size) * self.cell_size + self.half_cell
        self.y = rnd.randint(1, (self.window_height - 20)//self.cell_size) * self.cell_size + self.half_cell
        self.pos =(self.x, self.y)
        self.vizible = True

    def snake_tail_pos(self):
        pass