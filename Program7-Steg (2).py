#Program 7 - Steg Peter Ford Python2.7
#libraries
import sys
import math

#Constants
DEBUG = True
SENTINEL=bytearray([0,255,0,0,255,0])

#pulls command line arguments and parses/formats them for use
def processCommandLine():
	arguments = sys.argv
	try:
		i=1
		function=arguments[i][1:];i+=1
		mode=arguments[i][1:];i+=1
		#optinal arguments must be checked for or given a default value
		if(arguments[i][0:2]=='-o'):
			offset=arguments[i][2:];i+=1
		else:
			offset=0
		if(arguments[i][0:2]=='-i'):
			interval=arguments[i][2:];i+=1
		else:
			interval=1
		#file descriptor arguments must be opened and parsed into bytearrays
		wrapper=bytearray(open(arguments[i][2:],'r').read());i+=1
		#only need a hidden file if storing
		if(function=="s"):
			hidden=bytearray(open(arguments[i][2:],'r').read())
		else:
			hidden=""
	except Exception as ex:
		print "error reading command line, Proper usage is 'python Steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>] -s store -r retrieve -b bit mode -B byte mode -o<val> set offset to <val> (default is 0) -i<val> set interval to <val> (default is 1) -w<val> set wrapper file to <val> -h<val> set hidden file to <val>' \nThe error that was invoked is below:"
		print ex
	if DEBUG:
		print "function="+str(function)+" mode="+str(mode)+" offset="+str(offset)+" interval="+str(interval)+ " wrapper file(starts)="+str(wrapper[0:100])+" hidden file(starts)="+str(hidden[0:100])
	return function,mode,offset,interval,wrapper,hidden

#stores data using Byte method, based on peusdo-code in notes
def byteStore(wrapper, hidden, offset, interval):
	i=0
	while(i< len(hidden)):
		wrapper[offset] = hidden[i]
		offset += interval
		i+=1
	i=0
	while(i< len(SENTINEL)):
		wrapper[offset] = SENTINEL[i]
		offset += interval
		i+=1
	print wrapper

#Extracts data using Byte method, based on peusdo-code in notes
def byteExtract(wrapper, offset, interval):
	hidden=[None] *(int(math.ceil(len(wrapper)-offset/interval)))
	i=0
	while(offset<len(wrapper)):
		byte=wrapper[offset]
		hidden[i]=byte
		if(i>6):
			if(bytearray(hidden[i-6:i])==SENTINEL):
				break
		offset+=interval
		i+=1
	print bytearray(hidden[0:i-6])

#stores data using bit method, based on peusdo-code in notes
def bitStore(wrapper, hidden, offset, interval):
	i=0
	while(i<len(hidden)):
		j=0
		while(j<8):
			wrapper[offset] &= 11111110
			wrapper[offset] |= ((hidden[i] &10000000)>> 7)
			hidden[i]  = (hidden[i]  << 1) & ((2**8)-1)
			offset+= interval
			j+=1
		i+=1
	i=0
	while(i< len(SENTINEL)):
		j=0
		while(j<8):
			wrapper[offset] &= 11111110
			wrapper[offset] |= ((SENTINEL[i] &10000000)>> 7)
			SENTINEL[i] = (SENTINEL[i] << 1) & ((2**8)-1)
			offset+= interval
			j+=1
		i+=1
	print wrapper


#Extracts data using bit method, based on peusdo-code in notes
def bitExtract(wrapper, offset, interval):
	hidden=[None] *(int(math.ceil(len(wrapper)-offset/interval))+int(math.ceil(len(wrapper)-offset/interval))/10)
	i=0
	while (offset<len(wrapper)):
		j=0
		byte=0
		while(j<8):
			#take lsb for relavent byte
			byte |= (wrapper[offset] & 00000001)
			if(j<7):
				#move over what you have by a place and move down the wrapper
				byte = (byte <<1) & ((2**8)-1)
				offset += interval
			j+=1
		hidden[i]=byte
		offset += interval
		#if there are at least 6 bytes check the last section for the Sentinel
		if(i>6):
			if(bytearray(hidden[i-6:i])==SENTINEL):
				break
		i+=1
	print bytearray(hidden[:i-6])

#######################################################################################################
def Main():
	function, mode, offset, interval, wrapper, hidden = processCommandLine()
	if(mode=="B"):
		if(function=="s"):
			byteStore(wrapper, hidden, int(offset), int(interval))
		if(function=="r"):
			byteExtract(wrapper, int(offset), int(interval))
	if(mode=="b"):
		if(function=="s"):
			bitStore(wrapper, hidden, int(offset), int(interval))
		if(function=="r"):
			bitExtract(wrapper,int(offset), int(interval))

	

Main()