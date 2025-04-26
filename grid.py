# class grid
import pygame


class Grid:
    def __init__(self, colors, screen, window_width, window_height, cell_size):
        self.color = colors['COLOR_GRID']
        self.surface = screen
        self.window_width = window_width
        self.window_height = window_height
        self.cell_size = cell_size
    
    def show(self):
        for y in range(40, self.window_height, self.cell_size):
            pygame.draw.line(self.surface, self.color, (0, y), (self.window_width, y), width=1)
        for x in range(0, self.window_width, self.cell_size):
            pygame.draw.line(self.surface, self.color, (x, 40), (x, self.window_height), width=1)
