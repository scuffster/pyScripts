#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
	GPIO.output(11, True)
	time.sleep(2)
	GPIO.output (11, False)
	time.sleep(1)
