#!/usr/bin/env python
import sys, socket, time, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
##

##
# main
##

# pulse to C
GPIO.output(7,1) #
time.sleep(15)
GPIO.output(7, 1) #

