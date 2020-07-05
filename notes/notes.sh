

#disable cursor from blinking
#https://unix.stackexchange.com/a/27232
echo 0 > /sys/class/graphics/fbcon/cursor_blink

# the ANSI reset command for a terminal
#https://superuser.com/a/640340
printf "\033c" > /dev/tty0


# https://github.com/adafruit/Adafruit_CircuitPython_framebuf only supports 1 bit color


# use to display image on frame buffer
# https://elinux.org/EBC_Exercise_12a_2.4_TFT_LCD_display_via_SPI#Displaying_Images
fbi -noverbose -T 1 -a boris.png


# write random colors to framebuffer
cat /dev/urandom >/dev/fb0