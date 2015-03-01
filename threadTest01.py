#!/usr/bin/env python

import thread
import time

import pygame
import RPi.GPIO as GPIO

pygame.init()
pygame.mixer.music.load("effect.mp3")
scream = pygame.mixer.Sound("effect.mp3")
scream.set_volume(1.0)

# Define a function for the thread
def do_the_scream( threadName, delay):
#   pygame.mixer.music.load("effect.mp3")
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
try:
   thread.start_new_thread( do_the_scream, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass

