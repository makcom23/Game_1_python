from abc import ABC, abstractmethod
import pygame

class AbstractSnake(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def create(self, x, y):
        pass

    @abstractmethod
    def check_borders(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def check(self):
        pass

    def game_over(self):
        if self.pos in self.tail_pos[1:]:
            pygame.mixer.Sound.play(self.lose_sound) # sound lose
            pygame.time.delay(2000)
            pygame.mixer.Sound.play(self.game_over_sound) # sound game over
            text = pygame.font.SysFont('Orbitron', 50)
            img = text.render('GAME OVER', True, self.COLOR_STATUSBAR)
            self.surface.blit(img, (210, 250))
            pygame.display.update() 
            pygame.time.delay(5000)
            self.settings.set_setting('game_state', 0)
