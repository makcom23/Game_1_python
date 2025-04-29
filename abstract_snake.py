from abc import ABC, abstractmethod

class AbstractSnake(ABC):
    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def tail_show(self):
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

    @abstractmethod
    def game_over(self):
        pass
