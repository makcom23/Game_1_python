# class first window
import pygame
import button as bt
import sys
import settings as stts
import info_window as infwin

class Window:
    def __init__(self, surface, colors, settings, apple, start_game):
        
        self.surface = surface
        self.color = colors['COLOR_FIRSTWIND']
        self.font = pygame.font.SysFont(None, 36)
        self.color_font = colors['COLOR_WINDOW_FONT']
        self.info_window = infwin.info_window(self.surface, 'PLAYER NAME       SCORE')
        self.btn1 = bt.Button(self.surface, 'New player')
        self.btn2 = bt.Button(self.surface, 'Start game')
        self.btn3 = bt.Button(self.surface, 'Quit')
        self.btn1.is_active = True
        self.settings = settings
        self.apple = apple
        self.start_game = start_game

    def show(self, events):
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
                        self.apple.create()
                        self.start_game(self.apple)
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

                
