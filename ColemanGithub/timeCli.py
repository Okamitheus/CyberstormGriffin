########################
# Name: Coleman Levy
# Date: 4/11/2020
# Description: a program in Python 2 that receives and
#              decodes a time-based covert message
########################
import socket
from binascii import unhexlify
from sys import stdout
from time import time

#Debug mode for checking out the time between characters
DEBUG = False

#The Server's IP address and port
ip = "138.47.102.67"
port = 54321

#The assumed time difference between characters that will
#be turned into the covert message
ONE = 0.19
ZERO = 0.1

#Strings that will hold the covert message and the translation of 
#said message
covert_msg = ""
translate = ""

#Creates the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connects to the server
sock.connect((ip, port))

#Receives data until EOF
data = sock.recv(4096)

#Indicate this is about to be the overt message
print "Overt message: "

#While the data doesn't equal to EOF
while (data.rstrip("\n") != "EOF"):
    #Output the data
    stdout.write(data)
    stdout.flush()
    #Start the "timer", get more data, and end the "timer"
    t0 = time()
    data = sock.recv(4096)
    t1 = time()
    #Calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    #If the time between the characters was larger than ONE...
    if (delta >= ONE):
        #Add a one to the covert message
        covert_msg += "1"
    #Otherwise...
    else:
        #Add a zero to the covert message
        covert_msg += "0"
    #If debug mode is on...
    if (DEBUG):
        #Also output the time difference between each character
        stdout.write(" {}\n".format(delta))
        stdout.flush()

#The int for iterating through the covert message
i = 0
#The int that helps in translating the covert message
n = 0

#Goes through the entire covert message, one by one
while (i < len(covert_msg)):
    #Process one byte at a time
    b = covert_msg[i:i+8]
    #Convert it to ASCII (if it fails to convert, print a "?" for that character)
    n = int("0b{}".format(b), 2)
    try:
        translate += unhexlify("{0:x}".format(n))
    except:
        translate += "?"
    #Stop at the string "EOF"
    i += 8

#Output the translation
print ""
print "Secret message: "
print translate

#Close the connection to the server
sock.close()
