import pygame
import sys
import grid
import apple as apl
import save_results
import window as w
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
settings = stts.Settings()

# game managing
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0    

# game settings
FPS = 15
pygame.init() # initialization of pygame


def main(): 
    global FPS_CLOCK
    global DISPLAY

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY.fill(COLOR_BACKGROUND)

    pygame.display.set_caption('Snake')

    grd = grid.Grid(GRID_COLOR, DISPLAY, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
    apple = apl.Apple(DISPLAY, CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT)
    fstwin = w.Window(DISPLAY, COLOR_FIRSTWIND, settings, apple, start_game)
    statbar = bar.StatusBar(DISPLAY, COLOR_STATUSBAR, COLOR_BACKGROUND, settings)
    newplayer = np.NewPlayer(DISPLAY, settings)
   
    run_game(grd, apple, fstwin, statbar, newplayer)


def run_game(grd, apple, fstwin, statbar, newplayer):
    while True:
        DISPLAY.fill(COLOR_BACKGROUND)
        game_state = settings.get_setting('game_state')

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_state == 0:
                        terminate()
                    elif game_state == 1:
                        settings.set_setting('game_state', 0)
                    elif game_state == 2:
                        save_results(settings)
                        settings.set_setting('game_state', 0)

            if event.type == pygame.QUIT:
                terminate()

        match game_state:
            # main window
            case  0:
                fstwin.show(events)
            # new player
            case  1:
                newplayer.show(events)
            # game in progress
            case 2:
                grd.show()
                apple.show()
                statbar.show()


        FPS_CLOCK.tick(FPS)
        pygame.display.flip()
        

def save_results(settings):
    # Save the results to a file or database
    pass

def start_game(apple):
    apple.create()
    settings.set_setting('game_state', 2)
    settings.set_setting('score', 0)


def terminate():
    pygame.quit()
    sys.exit()


main()