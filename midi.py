# controlling the Adafruit Music Maker FeatherWing
# uses VS1053 chip

# going to use MIDI pin since the other pins are used by display
# and I don't need their funcationality
# !!! apply solder jumper on MIDI jumper
# https://learn.adafruit.com/adafruit-music-maker-featherwing/midi-synth#solder-closed-midi-jumper-2292069-2

# MIDI pin is on the UART TX pin
# this UART is /dev/ttyS0
# which is also the default debug UART on GiantBoard
# so startup messages may confuse the Music Maker
# if so, there's a reset pin
# (which is currently connected to system reset, so cut jumper if needed)

import serial

# MIDI uses baud rate 31250 KBaud
ser = serial.Serial('/dev/ttyS0', baudrate=31250)

# write data this way:
#ser.write(b'world\n\r')