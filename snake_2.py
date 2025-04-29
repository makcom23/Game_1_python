import pygame
import sys
import random as rnd
from abstract_snake import AbstractSnake

class Snake(AbstractSnake):
    def __init__(self, surface, colors, cell_size, window_width, window_height, settings, apple):
        super().__init__(surface, settings, window_width, window_height) 
        self.radius = 10
        self.eye = 2
        self.colors = colors
        self.COLOR_EYE = colors['COLOR_EYE']
        self.COLOR_SNAKE = colors['COLOR_SNAKE']
        self.COLOR_STATUSBAR = colors['COLOR_STATUSBAR']
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        self.x = 0
        self.y = 0
        self.pos = (self.x, self.y)
        self.apl = apple
        self.gameover = False
        self.head = None
        self.tail = None

    def show(self):
        if self.head == None:
            pygame.draw.circle(self.surface, self.COLOR_SNAKE, self.pos, self.radius, width=0) # snake's head
            pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x-3, self.y-3), self.eye, width=0) # snake's left eye
            pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x+3, self.y-3), self.eye, width=0) # snake's right eye
            pygame.draw.line(self.surface, self.COLOR_EYE, (self.x-3, self.y+6), (self.x+3, self.y+6), width=2) # snake's mouth
        else:
            pygame.draw.circle(self.surface, self.COLOR_SNAKE, self.pos, self.radius, width=0) # snake's tail
        
        if self.tail != None:
            self.tail.show()

    
    def move(self):
        direction = self.settings.get_setting('direction')
        pos = self.pos

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
            pygame.mixer.Sound.play(self.lose_sound) # sound lose
            pygame.time.delay(2000)
            pygame.mixer.Sound.play(self.game_over_sound) # sound game over
            text = pygame.font.SysFont('Orbitron', 50)
            img = text.render('GAME OVER', True, self.COLOR_STATUSBAR)
            self.surface.blit(img, (210, 250))
            pygame.display.update() 
            pygame.time.delay(5000)
            self.settings.set_setting('game_state', 0)
            
        if self.tail != None:
            self.tail.is_game_over(head)

    def check(self):
        if self.x == self.apl.x and self.y == self.apl.y:          
            self.apl.create()           
            score = self.settings.get_setting('score')
            score +=1
            self.settings.set_setting('score', score)
            pygame.mixer.Sound.play(self.crunch_sound) # sound apple crunch
            tail = self.tail
            self.tail = Snake(self.surface, self.colors, self.cell_size, self.window_width, self.window_height, self.settings, self.apl)
            self.tail.head = self
            self.tail.tail = tail
