#!/usr/bin/env python
import sys, socket, time, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
##
# state variables
##
CatzIn = False
LitzOn = False
i = 0

##
# main
##

# turn lights off
GPIO.output(11, False) #lights off

while not CatzIn:
  input_value = GPIO.input(12) # checking if cat flap is open
  if input_value == False:
     CatzIn = True
     print ("cat is in da house! ")
     GPIO.output(11, True) #lights on
     i = 0
     while CatzIn:
        i = i+1
#        os.system('vgrabbj -d /dev/video0 -f /home/pi/pyScripts/mnt/image'+str(i)+'.jpg')
        os.system('find /tmp/motion -type f -mmin -2|while read fname; do mv $fname /tmp/savedMotions; done')
#        os.system('rm /tmp/motion/*')
        print ("grab "+str(i)+"...")
        if i >= 5:
           CatzIn = False
           print ("Catz Out ")
     GPIO.output(11, False) #lights off
     print('lights off')
     while input_value == False:
	input_value = GPIO.input(12)
