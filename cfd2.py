#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from twython import TwythonStreamer
import tweepy
import twitter_monitor


# Search terms
TERMS = '#treatbebopblues'
terms_filename = "terms.txt"

# Twitter application authentication
APP_KEY = '7GUv0aiPBnH5DXC2hrtS1ssw5'
APP_SECRET = 'MdFrT55DXYMA2fQZwsnN8ckGEyXb4XRqVcDrsAaUq2wo2Ubx5w'
OAUTH_TOKEN = '15687368-IIoxPTnw6ItexxhLFWhApiNuw2ZCQbaXZvzJo9jka'
OAUTH_TOKEN_SECRET = 'PfvDvSD6OUMNcIy5Lj0Qca0M4UFRFtZ46rfJ4hAvO1n5D'

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
# while (True):
  # Change speed of continuous servo on channel O
  #pwm.setPWM(0, 0, servo1Min)
  #time.sleep(1)
  #pwm.setPWM(0, 0, servo1Max)
  #time.sleep(1)
  # Change speed of continuous servo on channel 15
  #pwm.setPWM(15, 0, servo2Min)
  #time.sleep(1)
  #pwm.setPWM(15, 0, servo2Max)
  #time.sleep(1)


# setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
        def on_success(self, data):
                if 'text' in data:
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
                        print data['text'].encode('utf-8')
                        print
                        #GPIO.output(LED, GPIO.HIGH)
                        #time.sleep(0.5)
                        #GPIO.output(LED, GPIO.LOW)

# Setup GPIO as output
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(LED, GPIO.OUT)
#GPIO.output(LED, GPIO.LOW)

# Create streamer
#while (True):
  # Change speed of continuous servo on channel O
  #pwm.setPWM(0, 0, servo1Min)
  #time.sleep(1)
  #pwm.setPWM(0, 0, servo1Max)
  #time.sleep(1)
  # Change speed of continuous servo on channel 15
  #pwm.setPWM(15, 0, servo2Min)
  #time.sleep(1)
  #pwm.setPWM(15, 0, servo2Max)
  #time.sleep(1)
  #print data['text'].encode('utf-8')
try:
        stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        stream.statuses.filter(track=TERMS)
except KeyboardInterrupt:
        GPIO.cleanup()
