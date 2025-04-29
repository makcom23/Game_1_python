import pygame
import sys
import grid
import apple as apl
import game_results
import window as w
import settings as stts
import status_bar as bar
import new_player as np
import snake_1 as snk
import game_time


# Размеры окна в пикселях
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# play zone 
PLAY_WIDTH = 800
PLAY_HEIGHT = 500

CELL_SIZE = 20

# Размеры сетки в ячейках
WIDTH = int(WINDOW_WIDTH / CELL_SIZE)
HEIGHT = int(WINDOW_HEIGHT / CELL_SIZE)

# Цвета
colors = {
'BG_COLOR' : (0, 0, 0),
'COLOR_GRID' : (40, 100, 40),
'COLOR_APPLE' : (200, 30, 30),
'COLOR_TAIL' : (30, 30, 30),
'APPLE_OUTER_COLOR' : (155, 0, 0),
'SNAKE_COLOR' : (0, 255, 0),
'SNAKE_OUTER_COLOR' : (0, 155, 0),
'COLOR_GREEN' : (0, 255, 0),
'COLOR_WHITE' : (255, 255, 255),
'COLOR_BLUE' : (0, 0, 255),
'COLOR_BACKGROUND' : (50, 30, 30),
'COLOR_FIRSTWIND' : (50, 80, 150),
'COLOR_STATUSBAR' : (180, 180, 180),
'COLOR_BORDER' : (50, 80, 150),
'COLOR_WINDOW_FONT' : (100, 150, 100),
'COLOR_SNAKE': (50, 200, 50),
'COLOR_EYE': (10, 10, 10),
}

# variables
settings = stts.Settings()

# game managing
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0    

# game settings
FPS = 3
pygame.init() # initialization of pygame


def main(): 
    global FPS_CLOCK
    global DISPLAY

    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    DISPLAY.fill(colors['COLOR_BACKGROUND'])

    pygame.display.set_caption('Snake')

    gametime = game_time.GameTime()
    grd = grid.Grid(colors, DISPLAY, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
    apple = apl.Apple(colors, DISPLAY, CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT)
    snake = snk.Snake(DISPLAY, colors, CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, settings, apple)
    fstwin = w.Window(DISPLAY, colors, settings, apple, start_game, snake)
    statbar = bar.StatusBar(DISPLAY, colors, settings, gametime)
    newplayer = np.NewPlayer(DISPLAY, settings)
   
    run_game(grd, apple, fstwin, statbar, newplayer, snake, gametime)


def run_game(grd, apple, fstwin, statbar, newplayer, snake, gametime):
    while True:
        DISPLAY.fill(colors['COLOR_BACKGROUND'])
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
                        game_results(settings)
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
                check_direction(events)
                grd.show()
                apple.show()
                statbar.show()
                snake.move()
                snake.show()
                snake.check()
                snake.tail_show()
                snake.game_over()
                gametime.start()


        FPS_CLOCK.tick(FPS)
        pygame.display.flip()

def check_direction(events): # привязка кнопок
    for event in events:
        if event.type == pygame.KEYDOWN:
            match event.key: 
                case pygame.K_UP:
                    settings.set_setting("direction", "up")
                case pygame.K_DOWN:
                    settings.set_setting("direction", "down")
                case pygame.K_LEFT:
                    settings.set_setting("direction", "left")
                case pygame.K_RIGHT:
                    settings.set_setting("direction", "right")


def game_results(settings):
    # Save the results to a file or database
    pass

def start_game(apple, snake):
    apple.create()
    snake.create(210, 510)
    settings.set_setting('direction', 'up')
    settings.set_setting('game_state', 2)
    settings.set_setting('score', 0)

def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()