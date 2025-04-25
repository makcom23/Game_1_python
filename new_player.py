import pygame_textinput
import pygame

class NewPlayer:
    def __init__(self, surface, settings):
        self.surface = surface
        self.settings = settings
        self.textinput = pygame_textinput.TextInputVisualizer()

    def show(self, events):
        self.textinput.update(events)
        self.surface.blit(self.textinput.surface, (200, 300))
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                name = self.textinput.value
                self.settings.set_setting('name', name)
                self.settings.set_setting('game_state', 0)




