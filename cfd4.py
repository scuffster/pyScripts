#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time
import tweepy
from datetime import datetime

# Search terms
TERMS = 'moretreats'

# How often to check the file for new terms
poll_interval = 70

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x40, debug=True)

servo1Min = 230  # Futaba S3003 Min pulse length out of 4096
servo1Max = 450  # Futaba S3003 Max pulse length out of 4096

# delay for dispenser to stay open
dispenseDelay = 0.5


def setServoPulse(channel, pulse):
    pulseLength = 1000000  # 1,000,000 us per second
    pulseLength /= 60  # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096  # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)


# Consumer keys and access tokens, used for OAuth
# Your twitter API credentials
consumer_key = '4UPhnXbXmqyUovLHct7mTvgHH'
consumer_secret = 'jenHT5Q3fk110LOvfRqH1bAD6MUEgMD404BV3WnMkWLoPYd2Fc'
access_token = '2900917134-P7VTOzA5eRP3PIqJQvrLnCckvFGoVcyDrx9xqeo'
access_token_secret = 'gojBf9W5iYWa6a8cmJa23Ktg9e376FWWpalhmszQ1479T'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

pwm.setPWMFreq(60)  # Set frequency to 60 Hz
while True:
    # delay
    time.sleep(poll_interval)

    # get latest tweet id for treats
    f = open('latestTreatTweetId')
    latestTreatTweetId = f.readline()
    f.close()

    # get the latest tweets since the last one
    try:
        user_tweets = api.mentions_timeline(latestTreatTweetId)
        dispenseTreat = False
        for tweet in user_tweets:
            # print 'tweet.id is: ',tweet.id
            #       print 'latestTreatTweetId is: ',latestTreatTweetId
            if int(tweet.id) > int(latestTreatTweetId):
                # print 'latestTreatTweetId is: ',latestTreatTweetId
                latestTreatTweetId = tweet.id  # store if this is a later tweet
            dispenseTreat = (tweet.text.find(TERMS) > -1)  # check whether the right hash tag (terms)
            print tweet.id, tweet.text, tweet.created_at, 'from: @', tweet.user.screen_name
    except Exception as e:
        print e.__doc__
        print e.message
        time.sleep(poll_interval)  # sleeping in case we've had a Tweepy error

    # write out the highest tweet id
    f = open('latestTreatTweetId', 'w')
    f.write(str(latestTreatTweetId))
    f.close()

    if dispenseTreat:
        print 'treat will be dispensed'
        # Change speed of continuous servo on channel O
        print "moving to open throw"
        pwm.setPWM(0, 0, servo1Min)
        time.sleep(dispenseDelay)
        print "moving to closed throw"
        pwm.setPWM(0, 0, servo1Max)
        time.sleep(dispenseDelay)
    else:
        print datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "no treats this time"

