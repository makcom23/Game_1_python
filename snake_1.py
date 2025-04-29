import pygame
import sys
import random as rnd
from abstract_snake import AbstractSnake

class Snake(AbstractSnake):
    def __init__(self, surface, colors, cell_size, window_width, window_height, settings, apple):
        super().__init__(surface, settings, window_width, window_height, colors, apple) 
        self.vizible = False
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        self.tail_pos = []
       

    def show(self):
        self.show_head()
    
    def tail_show(self):
        for pos in self.tail_pos[1:]:
            self.show_tail(pos)
        
    
    def move(self):

        self.direction()
        
        self.prev_head_pos = (self.x, self.y) # нужно список кортежей tail_pos как-то ограничить головой prev_head_pos и обрезать хвосты
        self.tail_pos.insert(0, self.prev_head_pos) 
        del self.tail_pos[self.tail_count+1:]

    def game_over(self):
        if self.pos in self.tail_pos[1:]:
            self.finish()
   
    def check(self):
        if self.apple_was_eaten():
            self.tail_count +=1