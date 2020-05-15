#Binary Decoder
#Katie Hay
#Version 2.7.15
from sys import stdin

def decode(binary, n):
    text = ""
    i = 0
    while (i < len(binary)):
        byte = binary[i:i+n]
        byte = int(byte, 2)
        #if backspace, remove last character of string
        if(byte == 8):
            text = text[:-1]
            i+=n
        else:
            text += chr(byte)
            i += n
    return text

binary = stdin.read().rstrip("\n")

if (len(binary) % 7 == 0):
    text = decode(binary, 7)
    print text
if (len(binary) % 8 == 0):
    text = decode(binary, 8)
    print text
