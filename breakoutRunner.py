import pygame, sys
from pygame.locals import *
from constants import *
from ball import *
from paddle import *
from bricks import *
from random import randint

pygame.init()
pygame.key.set_repeat(1)
screen = pygame.display.set_mode((screenSize, screenSize + GUISize))


def winCondition():
    pass


def keyPressed(paddle, left, right):
    keys = pygame.key.get_pressed()

    if keys[left]:
        paddle.move(-1)
    elif keys[right]:
        paddle.move(1)
    else:
        paddle.move(0)


while True:
    # Setup Code

    paddle = Paddle()
    ball = Ball()

    bricks = []
    y = GUISize + screenSize * .1
    color = 0
    level = 5
    for i in range(levelCount):
        bricks.append([])
        j = 0
        x = 0
        while x < screenSize:
            w = (randint(10, 20)) * level
            bricks[i].append(Bricks(x, y, w, i, j, colors[color]))
            x += w
        y += screenSize * .05
        color += 1
        level += 1

    # print(bricks)


    gameover = False
    setup = False

    while not setup:
        # Game loop
        while not gameover:
            # Game code
            screen.fill(black)

            paddle.draw(screen)

            ball.move(paddle)
            ball.draw(screen)
            ball.edgeBounce()

            if ball.y > screenSize + GUISize:
                ball.released = False
                ball.xspeed = 0
                ball.yspeed = -1

            if ball.collide(paddle):
                paddle.hit(ball)

            for i in bricks:
                for brick in i:
                    brick.draw(screen)

            if winCondition():
                gameover = True

            # GUI
            pygame.draw.line(screen, gray(200), (0, GUISize - 5), (screenSize, GUISize - 5), 5)

            pygame.display.update()

            # Input loop
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                keyPressed(paddle, K_a, K_d)

                if event.type == KEYDOWN and event.key == K_SPACE:
                    ball.released = True

        # Gameover loop


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_RETURN:
                gameover = False
                setup = True
