#!/usr/bin/env python
# ===============================================
# goldfish chat
# dscuffell, 20/01/2013
#
#
# ===============================================
# 1.0 : char : DS : 20/01/2013 : Initial version
# 1.5 : beta : DS : 26/01/2013 : extend if statment   
# ===============================================

# setup the GPIO board
# setup pin 11 for 3v o/p and switch transistor
#
import random 
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

#
#while True:
	#GPIO.output(11, True)
	#time.sleep(2)
	#GPIO.output (11, False)
	#time.sleep(1)

# setup the for irc 
# using wolfe.freenode.net
#
import socket
network = 'wolfe.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
# state variables
#
lights_on = False #boolean
time_to_quit = False #boolean
responded = False
# setup dictionary
#

# read from response dictionary
#
f = open(r'./fishResponses.txt')
i = 0
response = []
for line in f:
  response.append(line)

# main
print irc.recv ( 4096 )
irc.send ( 'NICK roger-the-fish\r\n' )
irc.send ( 'USER roger localhost localhost :winky sender\r\n' )
irc.send ( 'JOIN #goldfish\r\n' )
irc.send ( 'PRIVMSG #goldfish :Hello World.\r\n' )
GPIO.output(11, True)
lights_on = True
while True: #not time_to_quit :
   data = irc.recv ( 4096 )
   s = data
   responded = False
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )

   if data.find ( 'quit' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :Fine, if you dont want me\r\n' )
      time.sleep(1)
      GPIO.output(11, False)
      time.sleep(1)
      time_to_quit = True
      lights_on = False
      responded = True
      #irc.send ( 'QUIT\r\n' )

   if data.find ( 'reload vocab' ) != -1:
	# read from response dictionary
	#
	f = open(r'./fishResponses.txt')
	response = []
	for line in f:
  	   response.append(line)
        irc.send ( 'PRIVMSG #goldfish : how now brown cow  ...\r\n' )
        responded = True

   if data.find ( 'yo ' ) != -1:
      irc.send ( 'PRIVMSG #goldfish : yo my bro! hows it hang...\r\n' )
      if not lights_on:
        irc.send ( 'PRIVMSG #goldfish : it is dark in here ...\r\n' )
      responded = True

   if data.find ( 'hi ' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :yeah I already said hi...\r\n' )
      responded = True

   if data.find ( 'ello ' ) != -1:
      irc.send ( 'PRIVMSG #goldfish : hi...\r\n' )
      responded = True

   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #goldfish\r\n' )
      responded = True

   if data.find ( ' on' ) != -1:
      time.sleep(1)
      irc.send ( 'PRIVMSG #goldfish : ok ... \r\n' )
      GPIO.output(11, True)
      time.sleep(2)
      irc.send ( 'PRIVMSG #goldfish :... Hows that ...\r\n' )
      lights_on = True
      responded = True

   if (data.find ( 'light' ) != -1) and (data.find( ' off' ) != -1):
      print 'caught on request'
      if lights_on:
         print 'lights_on is true'
         time.sleep(1)
         irc.send ( 'PRIVMSG #goldfish : ok ... \r\n' )
         GPIO.output(11, False)
         time.sleep(2)
         irc.send ( 'PRIVMSG #goldfish :... alright for you, but I can''t see ...\r\n' )
         lights_on = False
      else:
         irc.send ( 'PRIVMSG #goldfish :...duh! the light is already off...\r\n' )
      responded = True

   if (data.find ( 'light' ) != -1) and (data.find( ' on ' ) != -1):
      if not lights_on:
         time.sleep(1)
         irc.send ( 'PRIVMSG #goldfish : ok ... \r\n' )
         GPIO.output(11, True)
         time.sleep(2)
         irc.send ( 'PRIVMSG #goldfish :... Hows that ...\r\n' )
         lights_on = True
      else:
         irc.send ( 'PRIVMSG #goldfish :...duh! the light is already on...\r\n' )
      responded = True
         
   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :WHERE!!!!!!\r\n' )
      responded = True

   if data.find ( 'slaps' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
      responded = True

   if not responded: 
      reply = random.choice(response)
      irc.send ( 'PRIVMSG #goldfish :I just don''t understand you ...'+reply+'\r\n' )
      responded = True

   print time.asctime() + data
