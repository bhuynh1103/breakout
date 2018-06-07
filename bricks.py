from pygame.draw import *
from constants import *


class Bricks:
    def __init__(self, x, y, w, i, j, color):
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.w = w
        self.h = screenSize * .05
        self.color = color

        if self.x + self.w > screenSize:
            self.w = screenSize - self.x

    def draw(self, window):
        rect(window, self.color, (self.x, self.y, self.w, self.h))
        rect(window, black, (self.x, self.y, self.w, self.h), 2)
