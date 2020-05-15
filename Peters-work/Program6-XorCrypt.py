#Program6-XorCrypt Peter Ford Python2.7
#bytearray
import sys
import binascii
import struct

#Constants
Debug=False

#lovely little blog explained this function and I nabbed it:"https://nitratine.net/blog/post/xor-python-byte-strings/"
def byte_xor(ba1, ba2):
    return bytearray([_a ^ _b for _a, _b in zip(ba1, ba2)])

#reads in Key from 'key' to a binaryarray
def getKey():
	key=open('key','r')
	keyArray=bytearray(key.read())
	key.close()
	if(Debug):
		print keyArray
	return keyArray

#reads in Text from Stdin to a binaryarray
def getText():
	text=bytearray(sys.stdin.read())
	if(Debug):
		print text
	return text

def Main():
	key=getKey()
	text=getText()
	while(len(text)>len(key)):
		key=key+key
	ciphertext=byte_xor(key,text)
	print ciphertext




Main()