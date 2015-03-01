#!/usr/bin/env python
import picamera
from time import sleep
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12,GPIO.IN)


camera = picamera.PiCamera()
camera.capture('image.jpg')

camera.start_preview()
#
#
#
#
#
i = 0
while i < 5760:
	camera.capture('ss'+str(i)+'.jpg')
	i = i+1
	sleep(5)
#
#GPIO.clearup


