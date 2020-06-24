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

# FLIR's Iron color palette
#https://stackoverflow.com/a/30066099
iron_palette = ["#1c0081","#1e0083","#200084","#220085","#240086","#260087","#280089","#2a0089","#2c008a","#2e008b","#30008c","#32008d","#34008e","#36008e","#38008f","#390090","#3b0091","#3c0092","#3e0093","#3f0093","#410094","#420095","#440095","#450096","#470096","#490096","#4a0096","#4c0097","#4e0097","#4f0097","#510097","#520098","#540098","#560098","#580099","#5a0099","#5c0099","#5d009a","#5f009a","#61009b","#63009b","#64009b","#66009b","#68009b","#6a009b","#6c009c","#6d009c","#6f009c","#70009c","#71009d","#73009d","#75009d","#77009d","#78009d","#7a009d","#7c009d","#7e009d","#7f009d","#81009d","#83009d","#84009d","#86009d","#87009d","#89009d","#8a009d","#8b009d","#8d009d","#8f009c","#91009c","#93009c","#95009c","#96009b","#98009b","#99009b","#9b009b","#9c009b","#9d009b","#9f009b","#a0009b","#a2009b","#a3009b","#a4009b","#a6009a","#a7009a","#a8009a","#a90099","#aa0099","#ab0099","#ad0099","#ae0198","#af0198","#b00198","#b00198","#b10197","#b20197","#b30196","#b40296","#b50295","#b60295","#b70395","#b80395","#b90495","#ba0495","#ba0494","#bb0593","#bc0593","#bd0593","#be0692","#bf0692","#bf0692","#c00791","#c00791","#c10890","#c10990","#c20a8f","#c30a8e","#c30b8e","#c40c8d","#c50c8c","#c60d8b","#c60e8a","#c70f89","#c81088","#c91187","#ca1286","#ca1385","#cb1385","#cb1484","#cc1582","#cd1681","#ce1780","#ce187e","#cf187c","#cf197b","#d01a79","#d11b78","#d11c76","#d21c75","#d21d74","#d31e72","#d32071","#d4216f","#d4226e","#d5236b","#d52469","#d62567","#d72665","#d82764","#d82862","#d92a60","#da2b5e","#da2c5c","#db2e5a","#db2f57","#dc2f54","#dd3051","#dd314e","#de324a","#de3347","#df3444","#df3541","#df363d","#e0373a","#e03837","#e03933","#e13a30","#e23b2d","#e23c2a","#e33d26","#e33e23","#e43f20","#e4411d","#e4421c","#e5431b","#e54419","#e54518","#e64616","#e74715","#e74814","#e74913","#e84a12","#e84c10","#e84c0f","#e94d0e","#e94d0d","#ea4e0c","#ea4f0c","#eb500b","#eb510a","#eb520a","#eb5309","#ec5409","#ec5608","#ec5708","#ec5808","#ed5907","#ed5a07","#ed5b06","#ee5c06","#ee5c05","#ee5d05","#ee5e05","#ef5f04","#ef6004","#ef6104","#ef6204","#f06303","#f06403","#f06503","#f16603","#f16603","#f16703","#f16803","#f16902","#f16a02","#f16b02","#f16b02","#f26c01","#f26d01","#f26e01","#f36f01","#f37001","#f37101","#f37201","#f47300","#f47400","#f47500","#f47600","#f47700","#f47800","#f47a00","#f57b00","#f57c00","#f57e00","#f57f00","#f68000","#f68100","#f68200","#f78300","#f78400","#f78500","#f78600","#f88700","#f88800","#f88800","#f88900","#f88a00","#f88b00","#f88c00","#f98d00","#f98d00","#f98e00","#f98f00","#f99000","#f99100","#f99200","#f99300","#fa9400","#fa9500","#fa9600","#fb9800","#fb9900","#fb9a00","#fb9c00","#fc9d00","#fc9f00","#fca000","#fca100","#fda200","#fda300","#fda400","#fda600","#fda700","#fda800","#fdaa00","#fdab00","#fdac00","#fdad00","#fdae00","#feaf00","#feb000","#feb100","#feb200","#feb300","#feb400","#feb500","#feb600","#feb800","#feb900","#feb900","#feba00","#febb00","#febc00","#febd00","#febe00","#fec000","#fec100","#fec200","#fec300","#fec400","#fec500","#fec600","#fec700","#fec800","#fec901","#feca01","#feca01","#fecb01","#fecc02","#fecd02","#fece03","#fecf04","#fecf04","#fed005","#fed106","#fed308","#fed409","#fed50a","#fed60a","#fed70b","#fed80c","#fed90d","#ffda0e","#ffda0e","#ffdb10","#ffdc12","#ffdc14","#ffdd16","#ffde19","#ffde1b","#ffdf1e","#ffe020","#ffe122","#ffe224","#ffe226","#ffe328","#ffe42b","#ffe42e","#ffe531","#ffe635","#ffe638","#ffe73c","#ffe83f","#ffe943","#ffea46","#ffeb49","#ffeb4d","#ffec50","#ffed54","#ffee57","#ffee5b","#ffee5f","#ffef63","#ffef67","#fff06a","#fff06e","#fff172","#fff177","#fff17b","#fff280","#fff285","#fff28a","#fff38e","#fff492","#fff496","#fff49a","#fff59e","#fff5a2","#fff5a6","#fff6aa","#fff6af","#fff7b3","#fff7b6","#fff8ba","#fff8bd","#fff8c1","#fff8c4","#fff9c7","#fff9ca","#fff9cd","#fffad1","#fffad4","#fffbd8","#fffcdb","#fffcdf","#fffde2"]
# count of colors
palette_count = len(iron_palette)-1

def calculateColor(temperature):
    global temp_max, temp_min

    # get range of temperatures from lowest to highest
    temp_range = temp_max - temp_min

    # subtract minimum to make the lowest temperature the lowest color
    temp_adj = temperature - temp_min

    # scale the temperature range to the color range
    t = (temp_adj / temp_range) * palette_count

    # convert to int so it ca be used as index
    t = int(t)

    #print(temperature, temp_adj, temp_min, temp_max, temp_range, t, palette_count)
    #print(iron_palette[t])

    return iron_palette[t]

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

#for row in range(8):
#    for column in range(8):
while True:
    # get a single reading so it doesn't change throughout drawing
    thermal_image = amg.pixels

    # get min/max temperature values
    temp_min = min([min(r) for r in thermal_image])
    temp_max = max([max(r) for r in thermal_image])
    #print("Min:", temp_min, "Max:", temp_max)

    for r, row in enumerate(thermal_image):
        print(["{0:.1f}".format(temp) for temp in row])
        # reverse to get the top/bottom orientation right
        for c, column in enumerate(reversed(row)):
            # convert the temperature to a color
            color = calculateColor(column)

            # display the rectangle at the cooresponding location
            pygame.draw.rect(screen, pygame.Color(color), pygame.Rect(ls+(gs*r), gs*c, gs-gap, gs-gap))


    # refresh the display
    pygame.display.flip()

    time.sleep(1)

#time.sleep(3)
# keep image on screen until done
#input("Press enter to exit...")