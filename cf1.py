#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servo1Min = 103  # Min pulse length out of 4096
servo1Max = 352  # Max pulse length out of 4096
servo2Max = 352  # Max pulse length out of 4096
servo2Min = 140  # Min pulse length out of 4096

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
while (True):
  print "Current Max is ",servo1Max
  x = raw_input("enter newMax: ") 
  if x is not None:
    servo1Max = x 
  print "servo1Max is ",servo1Max
  print "Current Min is ",servo1Min
  y = raw_input("enter newMin: ") 
  if y is not None:
    servo1min = y 
  print "servo1Min is ",servo1Min

  # Change speed of continuous servo on channel O
  pwm.setPWM(0, 0, servo1Min)
  time.sleep(1)
  pwm.setPWM(0, 0, servo1Max)
  time.sleep(1)
  # Change speed of continuous servo on channel 15
  pwm.setPWM(15, 0, servo2Min)
  time.sleep(1)
  pwm.setPWM(15, 0, servo2Max)
  time.sleep(1)

