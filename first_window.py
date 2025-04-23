# class first window
import pygame

class First_Window:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        self.rect_1 = (250, 100, 300, 50)
        self.rect_2 = (250, 200, 300, 50)
        self.rect_3 = (250, 300, 300, 50)
        self.font = pygame.font.SysFont(None, 36)
        self.color_font = (100, 150, 100)
        self.is_active = False

    def rectangles(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.is_active = True
                else:
                    self.is_active = False
                    

        if self.is_active:
            width =5 
        else: width=1

        rect1 = pygame.Rect(self.rect_1)
        pygame.draw.rect(self.surface, self.color, rect1, width, border_radius=5)
        center1 = rect1.center
        text1 = self.font.render('New player', True, self.color_font)
        text1_center = text1.get_rect(center=center1)
        self.surface.blit(text1, text1_center)

        rect2 = pygame.Rect(self.rect_2)
        pygame.draw.rect(self.surface, self.color, rect2, width, border_radius=5)
        center2 = rect2.center
        text2 = self.font.render('Start game', True, self.color_font)
        text2_center = text2.get_rect(center=center2)
        self.surface.blit(text2, text2_center)

        rect3 = pygame.Rect(self.rect_3)
        pygame.draw.rect(self.surface, self.color, rect3, width, border_radius=5)
        center3 = rect3.center
        text3 = self.font.render('Quit', True, self.color_font)
        text3_center = text3.get_rect(center=center3)
        self.surface.blit(text3, text3_center)