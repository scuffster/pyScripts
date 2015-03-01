#!/usr/bin/env python
import sys, socket, time, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT) #GP7
GPIO.setup(22,GPIO.OUT) #GP6
GPIO.setup(18,GPIO.OUT) #GP5
GPIO.setup(16,GPIO.OUT) #GP4
GPIO.setup(15,GPIO.OUT) #GP3
GPIO.setup(13,GPIO.OUT) #GP2
GPIO.setup(12,GPIO.OUT) #GP1
GPIO.setup(11,GPIO.OUT) #GP0
##
pin = [7,22,18,16,15,13,12,11]

##
# main
##

# pulse to C
for i in range(8) :
  GPIO.output(pin[i],True) #
  time.sleep(5)
  print("pin: ",pin[i])
  GPIO.output(pin[i],False) #

