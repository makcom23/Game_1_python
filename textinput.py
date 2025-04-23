# pygame textinput
import pygame
import pygame_textinput
pygame.init()

class text_input:
    def __init__(self, screen):
        self.screen = screen

    def input(self):
        textinput = pygame_textinput.TextInputVisualizer()

        screen = pygame.display.set_mode((400, 200))
        clock = pygame.time.Clock()

        while True:
            screen.fill((225, 225, 225))

            events = pygame.event.get()

            # Feed it with events every frame
            textinput.update(events)
            # Blit its surface onto the screen
            screen.blit(textinput.surface, (10, 10))

            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            pygame.display.update()
            clock.tick(30)
        
