import pygame
import snake as snk

class SnakeMove:
    def __init__(self, cell_size):
        self.snake = snk.Snake()
        self.pos = self.snake.snake_head_apears()
        self.cell_size = cell_size


    def snake_move(self, events, pos):
        x, y = self.pos
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y = y - self.cell_size
                elif event.key == pygame.K_DOWN:
                    y = y + self.cell_size
                elif event.key == pygame.K_LEFT:
                    x = x - self.cell_size
                elif event.key == pygame.K_RIGHT:
                    x = x + self.cell_size
        self.pos = (x,y)