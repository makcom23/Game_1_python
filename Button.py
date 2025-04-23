# class apple
import pygame
import random as rnd

class Button:
    def __init__(self, surface, text, width=300, height=50):
        self.surface = surface
        self.radius = 10
        self.COLOR_BORDER = (0, 255, 0)
        self.COLOR_BACKGROUND = (200, 30, 30)
        self.COLOR_SELECTED = (255, 0, 0)
        self.COLOR_TEXT = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.width = width
        self.height = height
        self.is_active = False

    def show_button(self, x, y):
        pygame.draw.rect(self.surface, self.COLOR_BORDER, (x, y, self.width, self.height), width=1, border_radius=5)
        img = self.font.render('First player', True, self.COLOR_TEXT)
        text_rectangle = img.get_rect()
        x = x + (self.width - text_rectangle.width) // 2
        y = y + (self.height - text_rectangle.height) // 2
        self.surface.blit(img, (x, y))
        if self.is_active:
            pygame.draw.rect(self.surface, self.COLOR_SELECTED, (x, y, self.width, self.height), width=10, border_radius=5)
        
    def set_active(self, is_active):
        self.is_active = is_active
        