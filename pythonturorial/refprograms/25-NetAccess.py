#
# read the data from the URL and print it --- Not working
#


'''
import urllib2
def main():
    # open a connection to a URL using urllib2
    webUrl = urllib.urlopen("https://www.youtube.com/user/guru99com")

    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print(data)


if(__name__ == "__main__"):
    main()
 '''
 
 
 
 #Used to make requests
import urllib.request

x = urllib.request.urlopen('http://kaushalya.tech/')
print(x.read())
 
 
 
 
'''
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()                # Close the connection
'''

# An example script to connect to Google using socket 
# programming in Python 
import socket # for socket 
import sys 

try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	print ("Socket successfully created")
except socket.error as err: 
	print ("socket creation failed with error %s" %(err))

# default port for socket 
port = 80

try: 
	host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 

	# this means could not resolve the host 
	print ("there was an error resolving the host")
	sys.exit() 

# connecting to the server 
s.connect((host_ip, port)) 

print ("the socket has successfully connected to google on port == %s" %(host_ip))
