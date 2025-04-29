import pygame_textinput
import pygame
import os
import json

class NewPlayer:
    def __init__(self, surface, settings):
        self.surface = surface
        self.settings = settings
        self.textinput = pygame_textinput.TextInputVisualizer()
        self.name = ''

    def show(self, events):
        self.textinput.update(events)
        self.surface.blit(self.textinput.surface, (250, 300))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.name = self.textinput.value
                #self.settings.set_setting('name', name)
                #self.settings.set_setting('game_state', 0)
        
        if os.path.exists('results.json'): # checking exist result.json
            with open('results.json') as res:
                results = json.load(res)
        else:
            results = {}    
        
        if self.name != results[self.name]: # checking exist name
            score = 0
            results.update({self.name: score})
        
        with open('results.json', 'w', encoding='utf-8') as res:
            json.dump(results, res, indent=4)




