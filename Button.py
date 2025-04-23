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
        self.text_surface = self.font.render(self.text, True, self.COLOR_TEXT)
        self.text_rect = self.text_surface.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.rect = pygame.Rect(self.text_rect.x - self.radius, self.text_rect.y - self.radius, self.text_rect.width + 2 * self.radius, self.text_rect.height + 2 * self.radius)
        self.width = width
        self.height = height

    def show_button(self, x, y):
        self.rect.topleft = (x, y)
        pygame.draw.rect(self.surface, self.COLOR_BORDER, (x, y, self.width, self.height), width=1, border_radius=5)
        img = self.font.render('First player', True, self.COLOR_TEXT)
        text_rectangle = img.get_rect()
        x = self.rect.x + (self.width - text_rectangle.width) // 2
        y = self.rect.y + (self.height - text_rectangle.height) // 2
        self.surface.blit(img, (x, y))
        