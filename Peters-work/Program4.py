#Peter Ford Python 2.7
import socket
from sys import stdout
from time import time
from binascii import unhexlify

#Constants
# enables debugging output
DEBUG = 0
ZERO = 0.025
ONE = .1


# set the server's IP address and port
ip = localhost
port = 1337

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
covert_bin=""
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write("{}".format(data))
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	if(delta >= ONE):
		covert_bin += "1"
	else:
		covert_bin += "0"
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

# close the connection to the server
s.shutdown(1)
s.close()

#Convert binary to ASCII
covert = ""
i = 0
while (i < len(covert_bin)):
	# process one byte at a time
	b = covert_bin[i:i + 8]
	# convert it to ASCII
	n = int("0b{}".format(b), 2)
	try:
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	# stop at the string "EOF"
	i += 8

#Print the covert message
print('\nCovert message is:')
i=0
#find the EOF and stop printing the hidden message so it doesn't repeat
for char in covert:
	if(covert[i:i+3]!= "EOF"):
		stdout.write("{}".format(char))
		stdout.flush()
	else:
		break
	i+=1
print('\n')


