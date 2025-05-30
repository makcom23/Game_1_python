# class first window
import pygame
import button as bt
import sys
import settings as stts
import info_window as infwin


class Window:
    def __init__(self, surface, colors, settings, apple, start_game, snake, gametime):
        
        self.surface = surface
        self.color = colors['COLOR_FIRSTWIND']
        self.font = pygame.font.SysFont(None, 36)
        self.color_font = colors['COLOR_WINDOW_FONT']
        self.info_window = infwin.info_window(self.surface, colors, 'PLAYER NAME       SCORE', settings)
        self.btn1 = bt.Button(self.surface, 'New player')
        self.btn2 = bt.Button(self.surface, 'Start game')
        self.btn3 = bt.Button(self.surface, 'Quit')
        self.btn4 = bt.Button(self.surface, 'Demo')
        self.btn1.is_active = True
        self.settings = settings
        self.apple = apple
        self.snake=snake
        self.start_game = start_game
        self.start_sound = pygame.mixer.Sound ("game_start.wav")
        self.gametime = gametime

    def show(self, events):
        self.info_window.show_window(250,50)
        self.btn1.show_button(250, 300)
        self.btn2.show_button(250, 400)
        self.btn3.show_button(250, 500)
        self.btn4.show_button2(50, 300)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # if press ENTER - go to other screen
                    if self.btn3.is_active:
                        pygame.quit()
                        sys.exit()
                    elif self.btn2.is_active:
                        self.start_game(self.apple, self.snake, self.gametime)
                        self.settings.set_setting('game_state', 2)
                        if self.settings.get_setting('sound'):
                            pygame.mixer.Sound.play(self.start_sound) # sound start game
                    elif self.btn1.is_active:
                        self.settings.set_setting('game_state', 1)
                    elif self.btn4.is_active:
                        self.start_game(self.apple, self.snake, self.gametime)
                        if self.settings.get_setting('sound'):
                            pygame.mixer.Sound.play(self.start_sound) # sound start game
                        self.settings.set_setting('game_state', 3) # demo

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

                if event.key == pygame.K_LEFT:
                    if self.btn1.is_active == True:
                        self.btn1.is_active = False
                        self.btn4.is_active = True

                if event.key == pygame.K_RIGHT:
                    if self.btn4.is_active == True:
                        self.btn4.is_active = False
                        self.btn1.is_active = True