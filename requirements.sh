#!/bin/bash
# restart script with root privileges if not already
[ "$UID" -eq 0 ] || exec sudo "$0" "$@" ]

# driver for thermal camera:
pip3 install adafruit-circuitpython-amg88xx

# for example (couldn't get it to work)
#pip3 install colour scipy