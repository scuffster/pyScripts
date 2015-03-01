#!/usr/bin/env python
import sys, socket, time
import RPi.GPIO as GPIO
RPL_NAMREPLY = '353'
RPL_ENDOFNAMES = '366'

irc = {	'host' : 'wolfe.freenode.net',
	'port': 6667,
	'channel' : '#goldfish',
	'namesinterval' : 10
}
user = {
	'nick' : 'scuffster-bot',
	'username' : 'derek-bot',
	'servername' : 'localhost',
	'hostname' : 'localhost',
	'realname' : 'winky names bot'
}

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'conneting to %(host)s:%(port)s...' % irc
try:
	s.connect((irc['host'], irc['port']))
except socket.error:
	print 'Error connecting to IRC server %(host) s:%(port)s' % irc
	sys.exit(1)

s.send('NICK %(nick)s\r\n' % user)
s.send ('USER %(username) s %(hostname) s %(servername) s :%(realname)s\r\n' % user)
s.send ('JOIN %(channel)s\r\n' % irc)
# s.send ('NAMES %(channel)s\r\n' % irc)

# now to create the recieve buffers etc
#
read_buffer = ''
names = []
while True:
	s.send ('NAMES %(channel)s\r\n' % irc)
	read_buffer += s.recv(1024)
	lines = read_buffer.split('\r\n')
	read_buffer = lines.pop();
	for line in lines:
		response = line.rstrip().split(' ',3)
		response_code = response[1]
		if response_code == RPL_NAMREPLY:
			names_list = response[3].split(':')[1]
			names += names_list.split(' ')
		if response_code == RPL_ENDOFNAMES:
			# display names then
			print '\r\nUsers in %(channel)s:' % irc
			for name in names:
				print name
			names = []
	time.sleep(irc['namesinterval'])
	s.send ('PRIVMSG %(channel)'+'Hello buffy' +'s\r\n' % irc)
	read_buffer += s.recv(1024)
	lines = read_buffer.split('\r\n')
	read_buffer = lines.pop();
	for line in lines:
		response = line.rstrip().split(' ',3)
		response_code = response[1]
		if response_code == RPL_NAMREPLY:
			names_list = response[3].split(':')[1]
			names += names_list.split(' ')
		if response_code == RPL_ENDOFNAMES:
			# display names then
			print '\r\nUsers in %(channel)s:' % irc
			for name in names:
				print name
			names = []
