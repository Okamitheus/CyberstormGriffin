########################
# Name: Coleman Levy
# Date: 3/24/2020
# Description: a program in Python 2 that decodes a binary string
########################
from sys import stdin

#The function that decodes the binary bytes
def decode(binary, n):
    #Initializing the return variable
    text = ""
    #Initializing the iterator
    i = 0
    #Loops as long as there are bytes left
    while (i < len(binary)):
        #Takes the current chunk of the binary string and separates it
        #into a single byte (size of byte depends on n)
        byte = binary[i:i+n]
        #Converts byte from binary to a decimal integer
        byte = int(byte, 2)
        #If the byte is a back space...
        if (byte == 8):
            #...delete the last character in text
            text = text[:-1]
        #Otherwise....
        else:
            #...convert the integer to its ASCII value and append
            #it to the end of text
            text += chr(byte)
        #Increase the iterator by n
        i += n
    #Once the loop is finished, return text
    return text

#Binary initializes as the string entered into the program minus the
#end line break
binary = stdin.read().rstrip("\n")

#If the binary string is a length divisible by 7...
if (len(binary) % 7 == 0):
    #...decode the binary as a 7-bit string
    text = decode(binary, 7)
    #Print that the binary is 7-bit and print what it was decoded as
    print "7-bit"
    print text
#If the binary string is a length divisible by 8...
if (len(binary) % 8 == 0):
    #...decode the binary as a 7-bit string
    text = decode(binary, 8)
    #Print that the binary is 8-bit and print what it was decoded as
    print "8-bit"
    print text

