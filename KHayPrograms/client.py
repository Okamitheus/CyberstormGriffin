#Katie Hay
#4/19/20
#Python 2.7

import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# set the server's IP address and port
IP = "localhost"
PORT = 4031

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((IP, PORT))

#Timings
ONE = 0.1
ZERO = 0.025

# receive data until EOF
data = s.recv(4096)
covert_bin = ""
while (data.rstrip("\n") != "EOF"):
	# output the data
	stdout.write(data)
	stdout.flush()
	# start the "timer", get more data, and end the "timer"
	t0 = time()
	data = s.recv(4096)
	t1 = time()
	# calculate the time delta (and output if debugging)
	delta = round(t1 - t0, 3)
	if (delta >= ONE):
		covert_bin += "1"
	else: 
		covert_bin += "0"
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

#Empty covert string
covert = ""
i = 0
while (i < len(covert_bin)):
	#process one byte at a time
	b = covert_bin[i:i+8]
	#convert to ASCII
	n = int("0b{}".format(b), 2)
	try:
		covert += unhexlify("{0:x}".format(n))
	except TypeError:
		covert += "?"
	#stop at the string "EOF"
	if (covert[-3:] == "EOF"):
		i = len(covert_bin)
	else:
		i += 8

#Take off the EOF from the covert message to show only the covert message
covert = covert[:-3]
stdout.write("Covert message: {}\n".format(covert))

# close the connection to the server
s.close()

