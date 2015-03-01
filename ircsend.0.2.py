import socket
network = 'wolfe.freenode.net'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK the-fish\r\n' )
irc.send ( 'USER scuff-send localhost localhost :winky sender\r\n' )
irc.send ( 'JOIN #goldfish\r\n' )
irc.send ( 'PRIVMSG #goldfish :Hello World.\r\n' )
while True:
   data = irc.recv ( 4096 )
   s = data
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( 'quit' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :Fine, if you dont want me\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'yo' ) != -1:
      irc.send ( 'PRIVMSG #goldfish : yo my bro! hows it hang...\r\n' )
   if data.find ( 'hi' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :yeah I already said hi...\r\n' )
   if data.find ( 'hello' ) != -1:
      irc.send ( 'PRIVMSG #goldfish : hi...\r\n' )
   if data.find ( 'KICK' ) != -1:
      irc.send ( 'JOIN #goldfish\r\n' )
   if data.find ( 'cheese' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :WHERE!!!!!!\r\n' )
   if data.find ( 'slaps' ) != -1:
      irc.send ( 'PRIVMSG #goldfish :This is the Trout Protection Agency. Please put the Trout Down and walk away with your hands in the air.\r\n' )
   print data
