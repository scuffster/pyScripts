import socket, time
network = 'wolfe.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK the-fish\r\n' )
irc.send ( 'USER scuff-send localhost localhost :winky sender\r\n' )
irc.send ( 'JOIN #goldfish\r\n' )
irc.send ( 'PRIVMSG #goldfish :Hello World.\r\n' )
i = 1
while True:
   i = i+1
   print str(i) + ': about to receive ...'
   time.sleep(1)
   data = irc.recv ( 4096 )
   print ' data received this is it ...'
   print data
   time.sleep(1)
   resp = raw_input('press return to continur ...')
   nickname = data[data.find(':')+1:data.find('!')] 
   print nickname
   msg = 'PRIVMSG #goldfish :' + nickname + ' yo my bro! hows it hang...\r\n'
   print 'going to send:' + msg
   if data.find ( 'PING' ) != -1:
      print '1'
      time.sleep(1)
      resp = raw_input('press return to continur ...')
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( 'quit' ) != -1:
      print '2'
      time.sleep(1)
      resp = raw_input('press return to continur ...')
      irc.send ( 'PRIVMSG #goldfish :Fine, if you dont want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'yo' ) != -1:
      print '3 we are in the yo section'
      time.sleep(1)
      resp = raw_input('press return to continur ...')
      msg = 'PRIVMSG #goldfish :' + nickname + ' yo my bro! hows it hang...\r\n'
      print 'going to send:' + msg
      print 'about to send '
      time.sleep(1)
      resp = raw_input('press return to continur ...')
      irc.send ( msg )
      print 'sent'
   if data.find ( 'hi' ) != -1:
      print '4'
      irc.send ( 'PRIVMSG #goldfish :yeah I already said hi...\r\n' )
   if data.find ( 'hello' ) != -1:
      print '5'
      irc.send ( 'PRIVMSG #goldfish : hi...\r\n' )
   if data.find ( 'KICK' ) != -1:
      print '6'
      irc.send ( 'JOIN #goldfish\r\n' )
   if data.find ( 'cheese' ) != -1:
      print '7'
      irc.send ( 'PRIVMSG #goldfish :WHERE!!!!!!\r\n' )
   if data.find ( 'slaps' ) != -1:
      print '8'
      irc.send ( 'PRIVMSG #goldfish :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   print data
