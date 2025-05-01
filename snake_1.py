import pygame
import sys
import random as rnd
import json
from abstract_snake import AbstractSnake

class Snake(AbstractSnake):
    def __init__(self, surface, colors, cell_size, window_width, window_height, settings, apple):
        super().__init__(surface, settings, window_width, window_height, colors, apple) 
        self.vizible = False
        self.cell_size = cell_size
        self.half_cell = cell_size // 2
        self.tail_pos = []
        self.window_width = window_width
        self.window_height = window_height
        self.win_sound = pygame.mixer.Sound ( "win.wav" )
       

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
        total_cells = self.window_width * (self.window_height-20) // self.cell_size**2
        occupied_cells = len(self.tail_pos)
        free_percent = ((total_cells - occupied_cells) / total_cells)*100  
        if self.pos in self.tail_pos[1:]:
            self.finish() # finish loose
        elif free_percent <= 97:
            self.win() # finish win
   
    def check(self):
        if self.apple_was_eaten():
            self.tail_count +=1

    def is_intersect_apple(self):
        if self.x == self.apl.x and self.y == self.apl.y:
            return True
        elif (self.apl.x, self.apl.y) in self.tail_pos:
                return True
        return False
    
    def win(self):
        
        if self.settings.get_setting('sound'):
            pygame.mixer.Sound.play(self.win_sound) # sound win
        text = pygame.font.SysFont('Orbitron', 50)
        img = text.render('YOU WIN!!!', True, self.COLOR_STATUSBAR)
        self.surface.blit(img, (250, 250))
        pygame.display.update() 
        pygame.time.delay(5000)

        # save game result #####################
        player_name = self.settings.get_setting('name')
        score = self.settings.get_setting('score')
        score = score * 2
        self.settings.set_setting('score', score)
        with open('results.json') as res:
            results = json.load(res)
        if score > results[player_name]: # check player result with exist results
            results[player_name] = score
    
            # sorting results.json
            sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True)) 
        
            with open('results.json', 'w', encoding='utf-8') as res:
                json.dump(sorted_results, res, indent=4)
        #####################
            
            self.settings.set_setting('game_state', 0)
        else:
            # exit
            self.settings.set_setting('game_state', 0)