#!/usr/bin/env python
import sys, socket, time
import RPi.GPIO as GPIO
s=':bebopblues!6d9af6b0@gateway/web/freenode/ip.109.154.246.176 PRIVMSG #goldfish :come on in slappy'
print 'hi '+s[s.find(':')+1:s.find('!')]
