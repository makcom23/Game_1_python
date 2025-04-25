# status bar

import pygame


class StatusBar:
    def __init__(self, surface, color, background, text,  position=(20, 20), fontsize=30):
        self.surface = surface
        self.COLOR_BORDER = (50, 80, 150)
        self.color = color
        self.text = text
        self.background = background
        self.position = position
        self.fontsize = fontsize

    def show_statusbar(self):
        text = pygame.font.Font(None, self.fontsize)
        img = text.render(self.text, True, self.color, self.background)
        self.surface.blit(img, self.position)
