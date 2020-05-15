#Katie Hay XOR Program 6
#5/1/20
#Python 2
from sys import stdin, stdout

#Modifiable key file
KEY = "key"

#Read the key file as binary data
key_file = open(KEY, "rb").read()

#Read the text through a buffer
text = (stdin.read())

j = 0
result = ""
#Cycle through the text, performing the xor operation on the ascii form of each character
for i in range(len(text)):
	result = result + "{}".format(chr(ord(text[i]) ^ ord(key_file[i])))

#Print the result through a buffer
stdout.write(result)
