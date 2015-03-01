#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
while True:
	input_value = GPIO.input(12)
	if input_value == False:
		print ("Button Press: input val is",input_value)
		print ("let the flashing commence! ")
		while input_value == False:
			input_value = GPIO.input(12)
