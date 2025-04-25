# status bar

import pygame


class StatusBar:
    def __init__(self, surface, color, background, settings,  position=(20, 20), fontsize=30):
        self.surface = surface
        self.COLOR_BORDER = (50, 80, 150)
        self.color = color
        self.settings = settings
        self.background = background
        self.position = position
        self.fontsize = fontsize

    def show_statusbar(self):
        name = self.settings.get_setting("name")
        score = self.settings.get_setting("score")
        sound = "on" if self.settings.get_setting("sound") else "off"
        msg = f'{name}: {score} apples            sound: {sound}            game time: 00:00:59'
        text = pygame.font.Font(None, self.fontsize)
        img = text.render(msg, True, self.color, self.background)
        self.surface.blit(img, self.position)
