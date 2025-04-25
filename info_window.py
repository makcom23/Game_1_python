import pygame

class info_window:
    def __init__(self, surface, colors, text, width=300, height=200):
        self.surface = surface
        self.COLOR_BORDER = colors['COLOR_FIRSTWIND']
        self.COLOR_TEXT = (100, 150, 100)
        self.width = width
        self.height = height
        self.text = text

    def show_window(self, x, y):
        
        info_window = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(self.surface, self.COLOR_BORDER, info_window, width=1, border_radius=5)
        
        font = pygame.font.Font(None, 30)
        img = font.render(self.text, True, self.COLOR_TEXT)
        pos_img = img.get_rect()
        x1 = x + (self.width - pos_img.width) //2
        
        self.surface.blit(img, (x1, y+20))

        
        
