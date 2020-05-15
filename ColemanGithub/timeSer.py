########################
# Name: Coleman Levy
# Date: 4/11/2020
# Description: a program in Python 2 that sends a time-based
#              covert message
########################
import socket
from time import sleep
from binascii import hexlify

#Small function that turns the covert message into binary
def covertify(message):
    #The return string
    covert_bin = ""
    #Sets string to equal the inputted message
    covert = message
    #Adds EOF to the end of the covert message
    covert += " EOF "
    #For each character in the covert message...
    for i in covert:
        #Convert to binary
        covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)
    #Return the converted message
    return covert_bin

#The overt message. Change this to change what the server sends.
msg = "Some message...\n"
#The covert message that this server sends.
covert_msg = "ABC"

#Sets the port for client connections
port = 1337

#Int that is used to to restart the covert message
#when necessary
n = 0

#Ints that decide how long the program sleeps between each character
ZERO = 0.025
ONE = 0.1

#Creates the socket and set it to the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", port))

#Listens for clients
sock.listen(0)

#When a client has connected...
c, addr = sock.accept()

#Convert the covert message to binary
covert_msg = covertify(covert_msg)
#Print the overt message to the server's user
print msg

#Send the overt message, one letter at a time
for i in msg:
    #Send the ith character of the overt message
    c.send(i)
    #If the current character of the covert message is a 0...
    if (covert_msg[n] == "0"):
        #Delay for ZERO's time until sending the next character
        sleep(ZERO)
    #Otherwise...
    else:
        #Delay for ONE's time...
        sleep(ONE)
    #Move to the next character in the covert message. If this goes past
    #the final character of the covert message, start back at the first character.
    n = (n + 1) % len(covert_msg)

#Send EOF
c.send("EOF")
#Wait a short time so the client can disconnect. This prevent the server's address
#from being occupied next time this program is run.
sleep(0.025)
#Close the server
c.close()
