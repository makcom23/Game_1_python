import pygame
import sys
import random as rnd
from abstract_snake import AbstractSnake

class Snake(AbstractSnake):
    def __init__(self, surface, colors, cell_size, window_width, window_height, settings, apple):
        self.vizible = False
        self.surface = surface
        self.radius = 10
        self.eye = 2
        self.COLOR_EYE = colors['COLOR_EYE']
        self.COLOR_SNAKE = colors['COLOR_SNAKE']
        self.COLOR_STATUSBAR = colors['COLOR_STATUSBAR']
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        self.window_width = window_width
        self.window_height = window_height
        self.settings = settings
        self.apl = apple
        self.crunch_sound = pygame.mixer.Sound ( "apple_crunch.wav" )
        self.lose_sound = pygame.mixer.Sound ( "lose.wav" )
        self.game_over_sound = pygame.mixer.Sound ( "game_over.wav" )
        self.tail_count = 0
        self.tail_pos = []
        self.gameover = False

    def show(self):
        pygame.draw.circle(self.surface, self.COLOR_SNAKE, self.pos, self.radius, width=0) # snake's head
        pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x-3, self.y-3), self.eye, width=0) # snake's left eye
        pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x+3, self.y-3), self.eye, width=0) # snake's right eye
        pygame.draw.line(self.surface, self.COLOR_EYE, (self.x-3, self.y+6), (self.x+3, self.y+6), width=2) # snake's mouth
    
    def tail_show(self):
        for pos in self.tail_pos[1:]:
            pygame.draw.circle(self.surface, self.COLOR_SNAKE, pos, self.radius, width=0) # snake's tail
        
    
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

    def move(self):

        direction = self.settings.get_setting('direction')

        match direction:
            case 'up': 
                self.y = self.y - self.cell_size
            case 'down':
                self.y = self.y + self.cell_size
            case 'left': 
                self.x = self.x - self.cell_size
            case 'right':
                self.x = self.x + self.cell_size
        self.check_borders()
        self.pos = (self.x, self.y)
        
        self.prev_head_pos = (self.x, self.y) # нужно список кортежей tail_pos как-то ограничить головой prev_head_pos и обрезать хвосты
        self.tail_pos.insert(0, self.prev_head_pos) 
        del self.tail_pos[self.tail_count+1:]
        #print(self.tail_pos)            

    def check(self):
    
        if self.x == self.apl.x and self.y == self.apl.y:          
            self.apl.create()           
            score = self.settings.get_setting('score')
            score += 1
            self.settings.set_setting('score', score)
            pygame.mixer.Sound.play(self.crunch_sound) # sound apple crunch
            self.tail_count +=1
        
  
           
