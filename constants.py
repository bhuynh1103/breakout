from pygame.font import Font

# Function for drawing text
def writeText(window, written, color, cenX, cenY, size):
    font = Font(None, int(size))
    text = font.render(written, 1, color)
    textpos = text.get_rect()
    textpos.centerx = cenX
    textpos.centery = cenY
    window.blit(text, textpos)
    return (textpos)

# Creates all gray-scale colors with one argument
def gray(x):
    return x, x, x


red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (127, 0, 255)
pink = (255, 0, 255)
black = gray(0)
white = gray(255)

# Brick colors
colors = [red, orange, yellow, green, blue, purple, pink]

# Constants
screenSize = 800
GUISize = screenSize // 10
borderThickness = int(screenSize * .05)
levelCount = 6
