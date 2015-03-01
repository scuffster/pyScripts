#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
i = 0
while i < 10:
	inVal = GPIO.input(12)
	print ("inval is",inVal)
	time.sleep(2)
	i = i+1

GPIO.clearup


