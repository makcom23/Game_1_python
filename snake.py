import pygame
import random
import sys
import grid
import apple
import save_results
import pygame_textinput
import textinput as txt

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
    apl = apple.Apple(DISPLAY)
    apl.creating_new_apple()
    text = txt.text_input(DISPLAY)

   
    run_game(grd, apl, text)


def run_game(grd, apl, text):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

        keys = pygame.key.get_pressed()
       
        # input name
        #save_res.save_name()

        # grid drawing
        grd.grid_drawing()

        # apple drawing
        apl.drawing_apple()

        #name input
        text.input()
        

        FPS_CLOCK.tick(FPS)
        pygame.display.flip()
        


def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()