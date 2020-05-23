#!/bin/bash   
# restart script with root privileges if not already
[ "$UID" -eq 0 ] || exec sudo "$0" "$@" ]

# move file with ip address already set up
# https://learn.adafruit.com/turning-your-raspberry-pi-zero-into-a-usb-gadget/ethernet-gadget
cp interfaces /etc/network/

ifdown usb0
ifup usb0