# class first window
import pygame
import button as bt
import sys
import settings as stts
import info_window as infwin

class First_Window:
    def __init__(self, surface, color, settings):
        
        self.surface = surface
        self.color = color
        self.font = pygame.font.SysFont(None, 36)
        self.color_font = (100, 150, 100)
        self.info_window = infwin.info_window(self.surface, 'PLAYER NAME       SCORE')
        self.btn1 = bt.Button(self.surface, 'New player')
        self.btn2 = bt.Button(self.surface, 'Start game')
        self.btn3 = bt.Button(self.surface, 'Quit')
        self.btn1.is_active = True
        self.settings = settings

    def rectangles(self, events):
        self.info_window.show_window(250,50)
        self.btn1.show_button(250, 300)
        self.btn2.show_button(250, 400)
        self.btn3.show_button(250, 500)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self.btn3.is_active:
                        pygame.quit()
                        sys.exit()
                    elif self.btn2.is_active:
                        self.settings.set_setting('game_state', 2)
                    elif self.btn1.is_active:
                        self.settings.set_setting('game_state', 1)

                if event.key == pygame.K_UP:
                    if self.btn1.is_active == True:
                        self.btn1.is_active = False
                        self.btn3.is_active = True

                    elif self.btn2.is_active == True:
                        self.btn2.is_active = False
                        self.btn1.is_active = True

                    elif self.btn3.is_active == True:
                        self.btn3.is_active = False
                        self.btn2.is_active = True

                if event.key == pygame.K_DOWN:
                    if self.btn1.is_active == True:
                        self.btn1.is_active = False
                        self.btn2.is_active = True

                    elif self.btn2.is_active == True:
                        self.btn2.is_active = False
                        self.btn3.is_active = True

                    elif self.btn3.is_active == True:
                        self.btn3.is_active = False
                        self.btn1.is_active = True

                
