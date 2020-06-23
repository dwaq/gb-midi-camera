import pygame
import sys
import os
import time

# get access to I2C
import board
import busio

# thermal camera library
import adafruit_amg88xx

# get thermal camera objects
i2c = busio.I2C(board.SCL, board.SDA)
amg = adafruit_amg88xx.AMG88XX(i2c)

# disable the mouse hardware
os.environ['SDL_NOMOUSE'] = '1'

# enable the display
pygame.display.init()

# get the display's capabilities (including resolution)
#print(pygame.display.Info())

# size of display
size = width, height = 480, 320

# hard code colors
black = 0, 0, 0

# turn off the mouse graphic
pygame.mouse.set_visible(0)

# screen object to display onto
screen = pygame.display.set_mode(size)

def displayText(text, size, color, clearScreen):

    if clearScreen:
        screen.fill(black)

    pygame.font.init()

    font = pygame.font.Font(None, size)
    text = font.render(text, 0, color)

    # only way to draw text is to overlay it using blit
    screen.blit(text, text.get_rect())

def calculateColor(temperature):
    # default values
    blue = 0
    red = 0

    red = (temperature-15)*(255/20)
    return (red, 0, 0)

    '''
    # temperature threshold
    tth = 20

    if (temperature < tth):
        # lower is more blue
        # (assumes min of 0)
        blue = (25-temperature)*(255/25)
        return (0, 0, blue)
    else:
        # higher is more red
        # must be between 20-30

    elif (temperature > 40):
    '''


#displayText('Giant Board', 30, (200,200,1), True)

# fill screen with any color
#screen.fill((100, 100, 100))

# draw on screen with color, location/size
#pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(25, 25, 25, 25))

# 8x8 grid of temperature values
# make a square using the full height (so 320x320 px)
# grid size = 320 pixel / 8 = 40
gs = 40

# starting position from left
ls = (width - height) / 2

# gap between rectangles
gap = 3

# get min/max temperature values
min_temp = min([min(r) for r in amg.pixels])
max_temp = max([max(r) for r in amg.pixels])
print("Min:", min_temp, "Max:", max_temp)

#for row in range(8):
#    for column in range(8):
while True:
    for r, row in enumerate(amg.pixels):
        print(["{0:.1f}".format(temp) for temp in row])
        for c, column in enumerate(row):
            # convert the temperature to a color
            color = calculateColor(column)

            # display the rectangle at the cooresponding location
            pygame.draw.rect(screen, color, pygame.Rect(ls+(gs*r), gs*c, gs-gap, gs-gap))


    # refresh the display
    pygame.display.flip()

    time.sleep(1)

#time.sleep(3)
# keep image on screen until done
#input("Press enter to exit...")