# controlling the Adafruit Music Maker FeatherWing
# uses VS1053 chip

from time import sleep

# going to use MIDI pin since the other pins are used by display
# and I don't need their funcationality
# MIDI pin is on the UART TX pin
# this UART is /dev/ttyS0
# which is also the default debug UART on GiantBoard
# so startup messages confuse the Music Maker
# so we need to reset the Music Maker after Linux is booted
# Rework Instructions:
# 1. Cut Reset pad (https://learn.adafruit.com/adafruit-music-maker-featherwing/pinouts#reset-jumper-and-pad-2992586-25)
#   1a. Reset line is normally connected to System reset which would cause the whole System to reset
# 2. Solder wire from RST via to adjacent pad (AD4)
#   2a. When looking at the bottom, there's a Via under the "f" in feather and connects to the via under the first "e" in feather
# 3. Apply solder jumper on MIDI jumper
#   3a. https://learn.adafruit.com/adafruit-music-maker-featherwing/midi-synth#solder-closed-midi-jumper-2292069-2

# reset the chip using General Purpose I/O
import board
from digitalio import DigitalInOut, Direction

reset = DigitalInOut(board.AD4)
reset.direction = Direction.OUTPUT
reset.value = False
sleep(0.01)
reset.value = True
sleep(0.01)

import serial

# MIDI uses baud rate 31250 KBaud
VS1053_MIDI = serial.Serial('/dev/ttyS0', baudrate=31250)

# Now convert player_miditest.ino to Python
# https://github.com/adafruit/Adafruit_VS1053_Library/blob/master/examples/player_miditest/player_miditest.ino

# See http://www.vlsi.fi/fileadmin/datasheets/vs1053.pdf Pg 31
VS1053_BANK_DEFAULT = 0x00
VS1053_BANK_DRUMS1 = 0x78
VS1053_BANK_DRUMS2 = 0x7F
VS1053_BANK_MELODY = 0x79

# See http://www.vlsi.fi/fileadmin/datasheets/vs1053.pdf Pg 32 for more!
VS1053_GM1_OCARINA = 80

MIDI_NOTE_ON =  0x90
MIDI_NOTE_OFF = 0x80
MIDI_CHAN_MSG = 0xB0
MIDI_CHAN_BANK = 0x00
MIDI_CHAN_VOLUME = 0x07
MIDI_CHAN_PROGRAM = 0xC0

def midiSetInstrument(chan, inst):
  #if (chan > 15) return
  inst-=1 # page 32 has instruments starting with 1 not 0 :(
  #if (inst > 127) return
  
  packet = bytearray()
  packet.append(MIDI_CHAN_PROGRAM | chan)  
  packet.append(inst)
  VS1053_MIDI.write(packet)

def midiSetChannelVolume(chan, vol):
  #if (chan > 15) return
  #if (vol > 127) return
  
  packet = bytearray()
  packet.append(MIDI_CHAN_MSG | chan)
  packet.append(MIDI_CHAN_VOLUME)
  packet.append(vol)
  VS1053_MIDI.write(packet)

def midiSetChannelBank(chan, bank):
  #if (chan > 15) return
  #if (bank > 127) return
  
  packet = bytearray()
  packet.append(MIDI_CHAN_MSG | chan)
  packet.append(MIDI_CHAN_BANK)
  packet.append(bank)
  VS1053_MIDI.write(packet)

def midiNoteOn(chan, n, vel):
  #if (chan > 15) return
  #if (n > 127) return
  #if (vel > 127) return
  
  packet = bytearray()
  packet.append(MIDI_NOTE_ON | chan)
  packet.append(n)
  packet.append(vel)
  VS1053_MIDI.write(packet)

def midiNoteOff(chan, n, vel):
  #if (chan > 15) return
  #if (n > 127) return
  #if (vel > 127) return
  
  packet = bytearray()
  packet.append(MIDI_NOTE_OFF | chan)
  packet.append(n)
  packet.append(vel)
  VS1053_MIDI.write(packet)

midiSetChannelBank(0, VS1053_BANK_MELODY)
midiSetChannelVolume(0, 127)
midiSetInstrument(0, VS1053_GM1_OCARINA)

'''
while True:
    for i in range(60, 69):
        midiNoteOn(0, i, 127)
        sleep(0.1)
        midiNoteOff(0, i, 127)

    sleep(1)
'''