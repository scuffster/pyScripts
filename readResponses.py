#!/usr/bin/env python
import sys, socket, time
import RPi.GPIO as GPIO
import random

f = open(r'./responses.txt')
i = 0
response = []
for line in f:
  response.append(line)
  i = i+1
  print ('line is: ' + line)
print (' and responses are: ')
for i in ['1','2','3']:
  print (random.choice(response))
