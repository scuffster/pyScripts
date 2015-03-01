## {{{ http://code.activestate.com/recipes/299411/ (r1)
import socket, string

#some user data, change as per your taste
SERVER = 'wolfe.freenode.net'
PORT = 6667
NICKNAME = 'scuffster-msg'
CHANNEL = '#goldfish'

#open a socket to handle the connection
IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
def irc_conn():
    IRC.connect((SERVER, PORT))

#simple function to send data through the socket
def send_data(command):
    IRC.send(command + '\n')

#join the channel
def join(channel):
    send_data("JOIN %s" % channel)

#send login data (customizable)
def login(nickname, username='bebop', password = None, realname='Dezza', hostname='wolfe', servername='wolfe.freenode.net'):
    send_data("USER %s %s %s %s" % (username, hostname, servername, realname))
    send_data("NICK " + nickname)

irc_conn()
login(NICKNAME)
join(CHANNEL)

while (1):
    buffer = IRC.recv(1024)
# - start
    #lines = buffer.split('\r\n')
    #buffer = lines.pop();
    #for line in lines:
          #response = line.rstrip().split(' ',3)
          #response_code = response[1]
          ## if response_code == RPL_NAMREPLY:
                 ## names_list = response[3].split(':')[1]
                 ## names += names_list.split(' ')
          ## if response_code == RPL_ENDOFNAMES:
                 ## # display names then
                 ## print '\r\nUsers in %(channel)s:' % irc
                 ##for name in names:
                         ##print name
                 ##names = []
          #print line
# - end
    msg = string.split(buffer)
#    lines = buffer.split('\r\n')
    #for line in lines:
        #print line
    if msg[0] == "PING": #check if server have sent ping command
        send_data("PONG %s" % msg[1]) #answer with pong as per RFC 1459
    if msg [1] == 'PRIVMSG' :
        filetxt = open('/tmp/msg.txt', 'a+') #open an arbitrary file to store the messages
        nick_name = msg[0][:string.find(msg[0],"!")] #if a private message is sent to you catch it
        print (nick_name)
        #send_data("PRIVMSG %s" % 'Hi there')
        IRC.send_data("PRIVMSG #goldfish :Hi There you\r\n")
        message = ' '.join(msg[3:])
#        filetxt.write(string.lstrip(nick_name, ':') + ' -> ' + string.lstrip(message, ':') + '\n') #write to the file
	print(string.lstrip(nick_name, ':') + ' -> ' + string.lstrip(message, ':') + '\n')
        filetxt.flush() #don't wait for next message, write it now!
## end of http://code.activestate.com/recipes/299411/ }}}

