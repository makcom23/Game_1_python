# class apple
import pygame
import random as rnd

class Button:
    def __init__(self, surface, text, width=300, height=50):
        self.surface = surface
        self.radius = 10
        self.COLOR_BORDER = (50, 80, 150)
        self.COLOR_BACKGROUND = (50, 30, 30)
        self.COLOR_SELECTED = (150, 30, 30)
        self.COLOR_TEXT = (100, 150, 100)
        self.font = pygame.font.Font(None, 36)
        self.text = text
        self.width = width
        self.height = height
        self.is_active = False

    def show_button(self, x, y):
        
        img = self.font.render(self.text, True, self.COLOR_TEXT)
        text_rectangle = img.get_rect()
        x1 = x + (self.width - text_rectangle.width) // 2
        y1 = y + (self.height - text_rectangle.height) // 2
        self.surface.blit(img, (x1, y1))
        if self.is_active:
           pygame.draw.rect(self.surface, self.COLOR_SELECTED, (x, y, self.width, self.height), width=5, border_radius=5)
        else: 
            pygame.draw.rect(self.surface, self.COLOR_BACKGROUND, (x, y, self.width, self.height), width=5, border_radius=5)
            pygame.draw.rect(self.surface, self.COLOR_BORDER, (x, y, self.width, self.height), width=1, border_radius=5)
        

        
    def set_active(self, is_active):
        self.is_active = is_active
        