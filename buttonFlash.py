#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

# while True:
	# GPIO.output(11, True)
	# time.sleep(2)
	# GPIO.output (11, False)
	# time.sleep(1)
# 
while True:
	# turns the lights off
	GPIO.output (11, False)
        lightFlashing = False
	input_value = GPIO.input(12)
	if input_value == False:
		print ("Button Press: input val is",input_value)
		print ("let the flashing commence! ")
                lightFlashing = True
		while input_value == False:
			# Turn the lights on
			GPIO.output(11, True)
			time.sleep(2)
			GPIO.output (11, False)
			time.sleep(1)
			input_value = GPIO.input(12)
		print ("Button Press: input val is",input_value)
		print ("let the flashing halt! ")
		
