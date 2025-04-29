import pygame_textinput
import pygame
import os
import json

class NewPlayer:
    def __init__(self, surface, settings, colors):
        self.surface = surface
        self.settings = settings
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.textinput.font_color = colors['COLOR_WINDOW_FONT']
        self.name = ''
        self.name_exist = False

    def show(self, events):
        self.textinput.update(events)
        self.surface.blit(self.textinput.surface, (300, 300))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.name = self.textinput.value
        
                # checking exist result.json
                if os.path.exists('results.json'):
                    with open('results.json') as res:
                        results = json.load(res)
                        results = dict(results)
                else:
                    results = {}    
                
                # checking exist name 
                if self.name in results:
                    self.settings.set_setting('name', self.name)   
                else:
                    score = 0
                    results.update({self.name: score})
                    self.settings.set_setting('name', self.name)
                    with open('results.json', 'w', encoding='utf-8') as res:
                        json.dump(results, res, indent=4)
                
                #goto first window
                self.settings.set_setting('game_state', 0)
                    





