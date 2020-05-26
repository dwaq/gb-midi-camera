#!/bin/bash
# restart script with root privileges if not already
[ "$UID" -eq 0 ] || exec sudo "$0" "$@" ]

# not using because I can't get numpy to install
# https://github.com/noisegate/fbpy
# https://pythonhosted.org/fbpy/

# get new numpy for Arm
pip3 install --extra-index-url=https://gergely.imreh.net/wheels/ numpy

# this numpy is old
apt install python-numpy libpng-dev libjack-dev
pip3 install Cython

git clone https://github.com/noisegate/fbpy.git
#git clone https://github.com/jackaudio/headers.git fbpy/fbpy/utils/jack
cd fbpy

# patch the files
# https://stackoverflow.com/a/2567610
sed -i '38i #define png_infopp_NULL (png_infopp)NULL' fbpy/utils/fbutils.c
sed -i '39i #define int_p_NULL (int*)NULL' fbpy/utils/fbutils.c

python3 setup.py install
