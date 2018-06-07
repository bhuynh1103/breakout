from pygame.draw import *
from constants import *
from random import uniform


class Paddle:
    def __init__(self):
        self.w = screenSize * .15
        self.h = self.w * .1
        self.x = screenSize // 2 - self.w // 2
        self.y = screenSize + GUISize - screenSize * .05
        self.speed = 5

    def draw(self, window):
        rect(window, white, (self.x, self.y, self.w, self.h))

    def move(self, direction):
        self.x += self.speed * direction

        if self.x < 0:
            self.x = 0
        elif self.x + self.w > screenSize:
            self.x = screenSize - self.w

    def hit(self, ball):
        interval = self.w // 8
        x = ball.x + ball.w

        if self.x <= x < self.x + interval or self.x <= x + ball.w < self.x + interval or self.x > ball.x + ball.w:
            # print(-3)
            ball.bounce(-1)
        elif self.x + interval * 1 <= x < self.x + interval * 2:
            # print(-2)
            ball.bounce(-2/3)
        elif self.x + interval * 2 <= x < self.x + interval * 3:
            # print(-1)
            ball.bounce(-1/3)
        elif self.x + interval * 3 <= x < self.x + interval * 5:
            # print(0)
            ball.bounce(uniform(-1/2, 1/2))
        elif self.x + interval * 5 <= x < self.x + interval * 6:
            # print(1)
            ball.bounce(1/3)
        elif self.x + interval * 6 <= x < self.x + interval * 7:
            # print(2)
            ball.bounce(2/3)
        elif self.x + interval * 7 <= x <= self.x + interval * 8 or self.x + self.h < ball.x:
            # print(3)
            ball.bounce(1)
