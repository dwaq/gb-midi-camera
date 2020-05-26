import pygame
import sys
import os
import time

os.environ['SDL_NOMOUSE'] = '1'

pygame.display.init()

#print(pygame.display.Info())

size = width, height = 480, 320
black = 0, 0, 0

pygame.mouse.set_visible(0)

screen = pygame.display.set_mode(size)

def displayText(text, size, line, color, clearScreen):

    """Used to display text to the screen. displayText is only configured to display
    two lines on the TFT. Only clear screen when writing the first line"""
    if clearScreen:
        screen.fill((0, 0, 0))

    pygame.font.init()

    font = pygame.font.Font(None, size)
    text = font.render(text, 0, color)

    textpos = text.get_rect()
    screen.blit(text, textpos)
    '''
    textRotated = pygame.transform.rotate(text, -90)
    textpos = textRotated.get_rect()
    textpos.centery = 80
    if line == 1:
         textpos.centerx = 90
         screen.blit(textRotated,textpos)
    elif line == 2:
        textpos.centerx = 40
        screen.blit(textRotated,textpos)
   '''

displayText('Outside Temp', 30, 1, (200,200,1), True)

#screen.fill((100, 100, 100))
#print("gonna draw")
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(25, 25, 25, 25))
pygame.display.flip()
#print("drew")

#time.sleep(3)
input("Press enter to exit...")