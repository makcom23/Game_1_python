import pygame
import sys
import random as rnd
from abstract_snake import AbstractSnake

class Snake(AbstractSnake):
    def __init__(self, surface, colors, cell_size, window_width, window_height, settings, apple):
        super().__init__(surface, settings, window_width, window_height, colors, apple) 
        self.colors = colors
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.head = None
        self.tail = None

    def show(self):
        if self.head == None:
           self.show_head()
        else:
            self.show_tail(self.pos)
        
        if self.tail != None:
            self.tail.show()

    
    def move(self):
        pos = self.pos
       
        self.direction()
        
        if (self.tail != None):
            self.tail.set_tail_pos(pos[0], pos[1])

    def set_tail_pos(self, x,y):
        tail = self.tail
        if tail != None:
            tail.set_tail_pos(self.x, self.y)
            
        self.x = x
        self.y = y
        self.pos = (x, y)

    def game_over(self):
        if self.tail != None:
            self.tail.is_game_over(self)

    def is_game_over(self, head):
        if head.pos == self.pos and head.tail != self:
            self.finish()
            
        if self.tail != None:
            self.tail.is_game_over(head)

    def check(self):
        if self.apple_was_eaten():
            
            tail = self.tail
            self.tail = Snake(self.surface, self.colors, self.cell_size, self.window_width, self.window_height, self.settings, self.apl)
            self.tail.head = self
            self.tail.tail = tail

    def is_intersect_apple(self):
        if self.x == self.apl.x and self.y == self.apl.y:
            return True
        else:
            if self.tail != None:
                return self.tail.is_intersect_apple()
            return False