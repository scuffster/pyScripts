#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
from twython import TwythonStreamer
import tweepy
import twitter_monitor


# Search terms
TERMS = '#treatbebopblues'
terms_filename = "terms.txt"

# How often to check the file for new terms
poll_interval = 15

# Your twitter API credentials
api_key = '7GUv0aiPBnH5DXC2hrtS1ssw5'
api_secret = 'MdFrT55DXYMA2fQZwsnN8ckGEyXb4XRqVcDrsAaUq2wo2Ubx5w'
access_token = '15687368-IIoxPTnw6ItexxhLFWhApiNuw2ZCQbaXZvzJo9jka'
access_token_secret = 'PfvDvSD6OUMNcIy5Lj0Qca0M4UFRFtZ46rfJ4hAvO1n5D'

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
#
# Construct your own subclasses here instead
listener = twitter_monitor.JsonStreamListener()
checker = twitter_monitor.FileTermChecker(filename=terms_filename)

# Start and maintain the streaming connection...
stream = twitter_monitor.DynamicTwitterStream(auth, listener, checker)
while True:
    try:
        # Loop and keep reconnecting in case something goes wrong
        # Note: You may annoy Twitter if you reconnect too often under some conditions.
        stream.start(poll_interval)
    except Exception as e:
        print e
        time.sleep(1)  # to avoid craziness with Twitter


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
