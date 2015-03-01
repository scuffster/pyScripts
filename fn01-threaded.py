#!/usr/bin/env python

import thread
import time

import pygame
import RPi.GPIO as GPIO

pygame.init()
pygame.mixer.music.load("effect.mp3")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

#scream = pygame.mixer.Sound("effect.mp3")
#scream.set_volume(1.0)

# Define a function for the thread
def do_the_scream (threadname, delay):
   pygame.mixer.music.load("effect.mp3")
   localtime = time.asctime( time.localtime(time.time()) )
   print ("Someone moved: ",input_value, localtime)
   pygame.mixer.music.play()
   time.sleep(2)
 



# Define a function for the thread
def x_do_the_scream( threadName, delay):
   pygame.mixer.music.load("effect.mp3")
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      localtime = time.asctime( time.localtime(time.time()) )
      print "%s: %s" % ( threadName, time.ctime(time.time()) )
      print ("Someone moved: ", localtime)
      pygame.mixer.music.play()
      time.sleep(2)

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )
      time.sleep(2)

# Create two threads as follows
while True:
        input_value = GPIO.input(12)
        if input_value == False:
                print ("Relay  closed: input val is",input_value)
                while input_value == False:
                        input_value = GPIO.input(12)
		try:
                  thread.start_new_thread( do_the_scream, ("Thread-1", 2, ) )
		except:
   		  print "Error: unable to start thread"

