#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time


# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

#servo1Min = 103  # Futaba S3003 Min pulse length out of 4096
#servo1Max = 352  # Futaba S3003 Max pulse length out of 4096

#servo1Min = 103  # Futaba S3003 Min pulse length out of 4096
servo1Min = 230  # Futaba S3003 Min pulse length out of 4096
servo1Max = 450  # Futaba S3003 Max pulse length out of 4096

servo2Max = 352  # Tower Pro SG90 Max pulse length out of 4096
servo2Min = 140  # Tower Pro SG90 Min pulse length out of 4096

dispenseDelay = 0.5

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

#while (True):

  #Change speed of continuous servo on channel O

print "moving to open throw" 
pwm.setPWM(0, 0, servo1Min)
time.sleep(dispenseDelay)

print "moving to closed throw" 
pwm.setPWM(0, 0, servo1Max)
time.sleep(dispenseDelay)

  #Change speed of continuous servo on channel 3
  #pwm.setPWM(12, 0, servo2Min)
  #time.sleep(1)
  #pwm.setPWM(12, 0, servo2Max)
  #time.sleep(1)

  #Change speed of continuous servo on channel 15
  #pwm.setPWM(15, 0, servo2Min)
  #time.sleep(1)
  #pwm.setPWM(15, 0, servo2Max)
  #time.sleep(1)
