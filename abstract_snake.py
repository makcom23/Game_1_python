from abc import ABC, abstractmethod
import pygame
import json

class AbstractSnake(ABC):

    def __init__(self, surface, settings, window_width, window_height, colors, apple, cell_size):
        self.surface = surface
        self.radius = 10
        self.eye = 2
        self.settings = settings
        self.window_width = window_width
        self.window_height = window_height
        self.tail_count = 0
        self.crunch_sound = pygame.mixer.Sound ( "apple_crunch.wav" )
        self.lose_sound = pygame.mixer.Sound ( "lose.wav" )
        self.game_over_sound = pygame.mixer.Sound ( "game_over.wav" )
        self.COLOR_EYE = colors['COLOR_EYE']
        self.COLOR_SNAKE = colors['COLOR_SNAKE']
        self.COLOR_STATUSBAR = colors['COLOR_STATUSBAR']
        self.apl = apple
        self.gameover = False
        self.cell_size = cell_size


    @abstractmethod
    def show(self):
        pass

    def show_head(self):
        pygame.draw.circle(self.surface, self.COLOR_SNAKE, self.pos, self.radius, width=0) # snake's head
        pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x-3, self.y-3), self.eye, width=0) # snake's left eye
        pygame.draw.circle(self.surface, self.COLOR_EYE, (self.x+3, self.y-3), self.eye, width=0) # snake's right eye
        pygame.draw.line(self.surface, self.COLOR_EYE, (self.x-3, self.y+6), (self.x+3, self.y+6), width=2) # snake's mouth

    def show_tail(self, pos):
        pygame.draw.circle(self.surface, self.COLOR_SNAKE, pos, self.radius, width=0) # snake's tail

    def direction(self):
        direction = self.settings.get_setting('direction')
        match direction:
            case 'up': 
                self.y = self.y - self.cell_size
            case 'down':
                self.y = self.y + self.cell_size
            case 'left': 
                self.x = self.x - self.cell_size
            case 'right':
                self.x = self.x + self.cell_size
        self.check_borders()
        self.pos = (self.x, self.y)

    def create(self, x, y):
        self.x = x
        self.y = y
        self.pos =(self.x, self.y)
        self.tail_pos = []  # обнуляем хвост
        self.tail_count = 0  # обнуляем длину хвоста
        self.vizible = True

    def check_borders(self):
        if self.y <= 40:
            self.y = self.window_height-10
        elif self.y >= self.window_height:
            self.y = 50
        elif self.x <= 0:
            self.x = self.window_width-10
        elif self.x >= self.window_width:
            self.x = 10

    def finish(self):
        if self.settings.get_setting('sound'): 
            pygame.mixer.Sound.play(self.lose_sound) # sound lose
        pygame.time.delay(2000)
        if self.settings.get_setting('sound'):
            pygame.mixer.Sound.play(self.game_over_sound) # sound game over
        text = pygame.font.SysFont('Orbitron', 50)
        img = text.render('GAME OVER', True, self.COLOR_STATUSBAR)
        self.surface.blit(img, (210, 250))
        pygame.display.update() 
        pygame.time.delay(5000)
        
        # save game result #####################
        player_name = self.settings.get_setting('name')
        score = self.settings.get_setting('score')
        with open('results.json') as res:
            results = json.load(res)
        if score > results[player_name]: # check player result with exist results
            results[player_name] = score
    
            # sorting results.json
            sorted_results = dict(sorted(results.items(), key=lambda item: item[1], reverse=True)) 
        
            with open('results.json', 'w', encoding='utf-8') as res:
                json.dump(sorted_results, res, indent=4)
            #####################
            
            self.settings.set_setting('game_state', 0)
        else:
            # exit
            self.settings.set_setting('game_state', 0)

        
    def apple_was_eaten(self):
        if self.is_intersect_apple():
            while True:
                self.apl.create()
                if self.is_intersect_apple() == False:
                    break
            score = self.settings.get_setting('score')
            score +=1
            self.settings.set_setting('score', score)
            if self.settings.get_setting('sound'): 
                pygame.mixer.Sound.play(self.crunch_sound) # sound apple crunch
            return True
        else:
            return False
        
    # DEMO FUNCTION *******************************************************************

    def move_demo(self):
        if self.x != self.apl.x:
            self.x = self.x + self.cell_size if self.x < self.apl.x else self.x - self.cell_size
        elif self.y != self.apl.y:
            self.y = self.y + self.cell_size if self.y < self.apl.y else self.y - self.cell_size

        self.check_borders()    
        self.pos = (self.x, self.y)

        self.prev_head_pos = (self.x, self.y) # обрезка хвоста
        self.tail_pos.insert(0, self.prev_head_pos) 
        del self.tail_pos[self.tail_count+1:] 

    def demo_game_over(self):
        total_cells = self.window_width * (self.window_height-20) // self.cell_size**2
        occupied_cells = len(self.tail_pos)
        free_percent = ((total_cells - occupied_cells) / total_cells)*100  
        if self.pos in self.tail_pos[1:]:
            self.settings.set_setting('game_state', 3) # finish loose
            self.create(210, 510)
            self.apl.create()
            self.move_demo()
           
        elif free_percent <= 95:
            self.win() # finish win

    
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def game_over(self):
        pass

    @abstractmethod
    def is_intersect_apple(self):
        pass

    def tail_show(self):
        pass