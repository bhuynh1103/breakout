from pygame.draw import *
from constants import *
from random import uniform


class Ball:
    def __init__(self):
        self.w = screenSize * .02
        self.x = screenSize // 2 - self.w // 2
        self.y = self.x + GUISize
        self.speed = 7.5
        self.xspeed = 0
        self.yspeed = -1
        self.released = False

    def draw(self, window):
        rect(window, gray(150), (self.x, self.y, self.w, self.w))
        if not self.released:
            line(window, white, (self.x + self.w // 2, self.y - self.w), (self.x + self.w // 2, self.y + self.w // 2), 1)

    def move(self, paddle):
        if not self.released:
            self.x = paddle.x + paddle.w // 2 - self.w // 2
            self.y = paddle.y - self.w * 1.5
        else:
            self.x += self.xspeed * self.speed
            self.y += self.yspeed * self.speed

    def edgeBounce(self):
        if self.x < 0 or self.x + self.w > screenSize:
            self.xspeed *= -1
        elif self.y < GUISize: # or self.y + self.w > screenSize + GUISize:
            self.yspeed *= - 1

    def bounce(self, xspeed):
        self.xspeed = xspeed
        self.yspeed = -1

    def collide(self, other):
        myTop = self.y
        myRight = self.x + self.w
        myBottom = self.y + self.w
        myLeft = self.x

        otherTop = other.y
        otherRight = other.x + other.w
        otherBottom = other.y + other.h
        otherLeft = other.x

        if myTop > otherBottom:
            return False
        elif myRight < otherLeft:
            return False
        elif myBottom < otherTop:
            return False
        elif myLeft > otherRight:
            return False
        else:
            return True
