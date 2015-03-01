#!/usr/bin/env python
import pygame
import time
import RPi.GPIO as GPIO
pygame.init()
pygame.mixer.music.load("effect.mp3")
#pygame.mixer.music.set_volume(1.0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
while True:
	input_value = GPIO.input(12)
	if input_value == False:
		print ("Relay  closed: input val is",input_value)
		while input_value == False:
			input_value = GPIO.input(12)
                        localtime = time.asctime( time.localtime(time.time()) )
		print ("Someone moved: ",input_value, localtime)
#                pygame.mixer.music.play()
                time.sleep(2)

