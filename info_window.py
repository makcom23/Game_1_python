import pygame
import json
from itertools import islice

class info_window:
    def __init__(self, surface, colors, text, settings, width=300, height=200):
        self.surface = surface
        self.COLOR_BORDER = colors['COLOR_FIRSTWIND']
        self.COLOR_TEXT = (100, 150, 100)
        self.COLOR_STATUSBAR = colors['COLOR_STATUSBAR']
        self.width = width
        self.height = height
        self.text = text
        self.settings = settings

    def show_window(self, x, y):
        
        info_window = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(self.surface, self.COLOR_BORDER, info_window, width=1, border_radius=5)
        
        font = pygame.font.Font(None, 30)
        img = font.render(self.text, True, self.COLOR_TEXT)
        pos_img = img.get_rect()
        x1 = x + (self.width - pos_img.width) //2
        self.surface.blit(img, (x1, y+20))

        # Players show in the first window

        with open('results.json') as res: # get sorted player's list
            my_dict = json.load(res)
            my_dict = dict(my_dict)
            #print(f'players: {results}')
        
        # get list from dict - first three names
        list_three = list(islice(my_dict.items(), 4))

        x1 = x + (self.width - self.width/100*85) //2
        
        player1 = font.render(list_three[0][0], True, self.COLOR_STATUSBAR)
        self.surface.blit(player1, (x1, y+60))
        
        player2 = font.render(list_three[1][0], True, self.COLOR_STATUSBAR)
        self.surface.blit(player2, (x1, y+90))
        
        player3 = font.render(list_three[2][0], True, self.COLOR_STATUSBAR)
        self.surface.blit(player3, (x1, y+120))

        player4 = font.render(list_three[3][0], True, self.COLOR_STATUSBAR)
        self.surface.blit(player4, (x1, y+150))

        # score
        x1 = x + (self.width - self.width/100*30)

        score1 = font.render(str(list_three[0][1]), True, self.COLOR_STATUSBAR)
        self.surface.blit(score1, (x1, y+60))
        
        score2 = font.render(str(list_three[1][1]), True, self.COLOR_STATUSBAR)
        self.surface.blit(score2, (x1, y+90))
        
        score3 = font.render(str(list_three[2][1]), True, self.COLOR_STATUSBAR)
        self.surface.blit(score3, (x1, y+120))

        score4 = font.render(str(list_three[3][1]), True, self.COLOR_STATUSBAR)
        self.surface.blit(score4, (x1, y+150))



        
        
