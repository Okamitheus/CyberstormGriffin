########################
# Name: Coleman Levy
# Date: 4/26/2020
# Description: a program in Python 3 that can encode and
#              decode a covert message with XOR and a key
########################
from sys import stdin
from sys import stdout

#The message input by the user to be en/decoded (taken in as a bytearray)
mes = bytearray(stdin.buffer.read())
#Opens the "key" file
file = open("key", "r")
#Takes in the "key" as a byte array
key = bytearray(file.buffer.read())

#The operation that XOR's the two byte arrays together
covert = bytes(a ^ b for (a, b) in zip(mes, key))

#Writes the newly created binary in its ascii form to
#a file or the terminal
stdout.buffer.write(covert)
print ("")
