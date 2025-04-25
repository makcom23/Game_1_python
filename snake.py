import pygame
import random
import sys
import grid
import apple
import save_results
import pygame_textinput
import first_window as fwnd
import settings as stts
import status_bar as bar
import new_player as np

# Размеры окна в пикселях
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

CELL_SIZE = 20

# Размеры сетки в ячейках
WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

# Цвета
BG_COLOR = (0, 0, 0)
GRID_COLOR = (40, 100, 40)
APPLE_COLOR = (255, 0, 0)
APPLE_OUTER_COLOR = (155, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SNAKE_OUTER_COLOR = (0, 155, 0)

COLOR_GREEN = (0, 255, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE = (0, 0, 255)
COLOR_BACKGROUND = (50, 30, 30)
COLOR_FIRSTWIND = (50, 80, 150)
COLOR_STATUSBAR = (180, 180, 180)

# variables
settings = stts.settings()

# game managing
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0    

# game settings
FPS = 15
pygame.init() # initialization of pygame


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main(): 
    global FPS_CLOCK
    global DISPLAY

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY.fill(COLOR_BACKGROUND)

    pygame.display.set_caption('Snake')

    #player_rect         = DISPLAY.get_rect(center=(WIDTH/2, HEIGHT/2))
    grd = grid.Grid(GRID_COLOR, DISPLAY, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
    apl = apple.Apple(DISPLAY, CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT)
    apl.creating_new_apple()
    fstwin = fwnd.First_Window(DISPLAY, COLOR_FIRSTWIND, settings)
    statbar = bar.StatusBar(DISPLAY, COLOR_STATUSBAR, COLOR_BACKGROUND, settings)
    newplayer = np.NewPlayer(DISPLAY, settings)
   
    run_game(grd, apl, fstwin, settings, statbar, newplayer)


def run_game(grd, apl, fstwin, settings, statbar, newplayer):
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                terminate()

        keys = pygame.key.get_pressed()
        game_state = settings.get_setting('game_state')
        
        # input name
        #save_res.save_name()

        # grid drawing
        if game_state == 2:
            DISPLAY.fill(COLOR_BACKGROUND)
            grd.grid_drawing()

        # apple drawing
            apl.drawing_apple()
        # status bar
            statbar.show_statusbar()

        #name input
        if game_state == 1:
            DISPLAY.fill(COLOR_BACKGROUND)
            newplayer.show(events)

        # first window
        if game_state == 0:
            DISPLAY.fill(COLOR_BACKGROUND)
            fstwin.rectangles(events)
    

        FPS_CLOCK.tick(FPS)
        pygame.display.flip()
        


def terminate():
    pygame.quit()
    sys.exit()


main()