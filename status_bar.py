# status bar

import pygame


class StatusBar:
    def __init__(self, surface, colors, settings, gametime, position=(20, 10), fontsize=30):
        self.surface = surface
        self.COLOR_BORDER = colors['COLOR_BORDER']
        self.color = colors['COLOR_STATUSBAR']
        self.settings = settings
        self.background = colors['COLOR_BACKGROUND']
        self.position = position
        self.fontsize = fontsize
        self.gmt = gametime

    def show(self):
        name = self.settings.get_setting("name")
        score = self.settings.get_setting("score")
        sound = "on" if self.settings.get_setting("sound") else "off"
        msg = f'{name}: {score} apples            sound: {sound}            game time:  {self.gmt.get_time()} '
        text = pygame.font.Font(None, self.fontsize)
        img = text.render(msg, True, self.color, self.background)
        self.surface.blit(img, self.position)
