#!/bin/bash

# Need cmake for FreeType
# & other dependencies
# https://stackoverflow.com/a/15368766sudo
apt install cmake libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev

# Install FreeType Raspberry Pi
# https://git.zsinfo.nl/snippets/8
wget -O - http://git.zsinfo.nl/snippets/8/raw | bash

# install pygame under sudo because it needs sudo to access framebuffer
# https://www.pygame.org/wiki/GettingStarted
sudo python3 -m pip install -U pygame

# driver for thermal camera:
sudo python3 -m pip install -U adafruit-circuitpython-amg88xx
