# class first window
import pygame

class First_Window:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        self.rect_1 = (250, 100, 300, 50)
        self.rect_2 = (250, 200, 300, 50)
        self.rect_3 = (250, 300, 300, 50)


    def rectangles(self):
        pygame.draw.rect(self.surface, self.color, self.rect_1, width=1, border_radius=5)
        font = pygame.font.SysFont(None, 36)
        img = font.render('First player', True, (100, 150, 100))
        self.surface.blit(img, self.rect_1)

        pygame.draw.rect(self.surface, self.color, self.rect_2, width=1, border_radius=5)
        pygame.draw.rect(self.surface, self.color, self.rect_3, width=1, border_radius=5)