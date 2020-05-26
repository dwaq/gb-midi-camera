import pygame
import sys
import os
import time

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

displayText('Giant Board', 30, (200,200,1), True)

# fill screen with any color
#screen.fill((100, 100, 100))

# draw on screen with color, location/size
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(25, 25, 25, 25))

# refresh the display
pygame.display.flip()

#time.sleep(3)
# keep image on screen until done
input("Press enter to exit...")