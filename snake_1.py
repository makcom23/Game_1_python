import pygame
import sys
import random as rnd
from abstract_snake import AbstractSnake

class Snake(AbstractSnake):
    def __init__(self, surface, colors, cell_size, window_width, window_height, settings, apple):
        super().__init__(surface, settings, window_width, window_height) 
        self.vizible = False
        self.eye = 2
        self.COLOR_EYE = colors['COLOR_EYE']
        self.COLOR_SNAKE = colors['COLOR_SNAKE']
        self.COLOR_STATUSBAR = colors['COLOR_STATUSBAR']
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        
        self.apl = apple
        
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

    def game_over(self):
        if self.pos in self.tail_pos[1:]:
            pygame.mixer.Sound.play(self.lose_sound) # sound lose
            pygame.time.delay(2000)
            pygame.mixer.Sound.play(self.game_over_sound) # sound game over
            text = pygame.font.SysFont('Orbitron', 50)
            img = text.render('GAME OVER', True, self.COLOR_STATUSBAR)
            self.surface.blit(img, (210, 250))
            pygame.display.update() 
            pygame.time.delay(5000)
            self.settings.set_setting('game_state', 0)
  
           
    def check(self):
        if self.x == self.apl.x and self.y == self.apl.y:          
            self.apl.create()           
            score = self.settings.get_setting('score')
            score +=1
            self.settings.set_setting('score', score)
            pygame.mixer.Sound.play(self.crunch_sound) # sound apple crunch
            self.tail_count +=1