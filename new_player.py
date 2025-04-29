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
        
                if os.path.exists('results.json'): # checking exist result.json
                    with open('results.json') as res:
                        results = json.load(res)
                else:
                    results = {}    
                
                if self.name in results: # checking exist name
                    self.name_exist = True
                else:
                    score = 0
                    results.update({self.name: score})
                    self.name_exist = False

                with open('results.json', 'w', encoding='utf-8') as res:
                    json.dump(results, res, indent=4)
                
                if self.name_exist == False:
                    self.settings.set_setting('game_state', 0)

        if self.name_exist: 
                    font = pygame.font.Font(None, 30)
                    warning_text = font.render('This name exists already, please use another name.', True, (200, 50, 50))
                    self.surface.blit(warning_text, (155, 350))
                    pygame.display.update()





