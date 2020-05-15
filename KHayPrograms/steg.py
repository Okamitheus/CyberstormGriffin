#Steg Program 7 - Python 2 
#Katie Hay
#5/6/20
#Execution (Storage): python steg.py -(s) -(b/B) -o(offset value) -i(interval value) -w(wrapper file) -h(hidden file)
#Execution (Retrieval): python steg.py -(r) -(b/B) -o(offset value) -i(interval value) -w(wrapper file)

from sys import stdin, stdout, argv

################ CONSTANTS ##################
SENTINEL = bytearray([0x00, 0xff, 0x00, 0x00, 0xff, 0x00])

################ FUNCTIONS ##################
#Byte Storage
def storeByte(INTERVAL, OFFSET, WRAPPER):
    #Grab the hidden file, read as binary data, throw an error if one is not specified
	try:
	    HIDDEN = open(argv[6][2:], 'rb').read()
	    HIDDEN = bytearray(HIDDEN)
	except:
	    print "Hidden file not found, please check your arguments."

	#Store the hidden file into the wrapper file
	i = 0
	while(i < len(HIDDEN)):
	    WRAPPER[OFFSET] == HIDDEN[i]
	    OFFSET += INTERVAL
	    i += 1

	i = 0
	while(i < len(SENTINEL)):
	    WRAPPER[OFFSET] == SENTINEL[i]
	    OFFSET += INTERVAL
	    i += 1
	return WRAPPER
	    
#Byte Extraction
def retreiveByte(INTERVAL, OFFSET, WRAPPER):
	#Empty byte array
	HIDDEN = bytearray()

        bits = bytearray()
        for x in range(0, 6):
            bits.append(WRAPPER[OFFSET])
            OFFSET += INTERVAL
        while (OFFSET < len(WRAPPER)):
            if(bits != SENTINEL):
                HIDDEN.append(bits[0])
                bits = bits[1:]
                bits.append(WRAPPER[OFFSET])
                OFFSET += INTERVAL
            else:
                return HIDDEN
        
##	#Grab each byte according to offset and interval
##	while (OFFSET < len(WRAPPER)):
##	    b = WRAPPER[OFFSET]           
##	    HIDDEN.append(b)    
##	    OFFSET += INTERVAL
##	    #Check if you hit the sentinel byte sequence
##	    hide = list(HIDDEN[-6:])
##	    if(hide == SENTINEL[0:(len(SENTINEL))]):
##		HIDDEN = HIDDEN[:-6]
##		OFFSET = len(WRAPPER)
##	return HIDDEN

	
#Bit Storage
def storeBit(INTERVAL, OFFSET, WRAPPER):
	#Grab the hidden file, read as binary data, throw an error if one is not specified
	try:
	    HIDDEN = open(argv[6][2:], 'rb').read()
	    HIDDEN = bytearray(HIDDEN)
	except:
	    print "Hidden file not found, please check your arguments."

	#Store the hidden file into the wrapper file
	i = 0
	while(i < len(HIDDEN)):
	    for k in range(0, 8):
		WRAPPER[OFFSET] &= 11111110
		WRAPPER[OFFSET] |= ((HIDDEN[i] & 10000000) >> 7)
		HIDDEN[i] = (HIDDEN[i] << 1) & (2 ** 8 - 1)
		OFFSET += INTERVAL
	    i += 1

	i = 0
	while(i < len(SENTINEL)):
	    for k in range(0, 8):
		WRAPPER[OFFSET] &= 11111110
		WRAPPER[OFFSET] |= ((SENTINEL[i] & 10000000) >> 7)
		SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
		OFFSET += INTERVAL
	    i += 1
	return WRAPPER
	    
#Bit Extraction
def retreiveBit(INTERVAL, OFFSET, WRAPPER):
	#Empty byte array
	HIDDEN = bytearray()

	bits = bytearray()
	#Grab each bit according to offset and interval
	for i in range(0, 6):
	    b = 0
	    for j in range(0, 8):
		b |= (WRAPPER[OFFSET] & 00000001)
		if (j < 7):
		    b = (b << 1) & (2 ** 8 - 1)
		    OFFSET += INTERVAL
	    bits.append(b)    
	    OFFSET += INTERVAL
	while(OFFSET < len(WRAPPER)):
            if(bits != SENTINEL):
                b = 0
                HIDDEN.append(bits[0])
                bits = bits[1:]
                for j in range(0, 8):
                    b |= (WRAPPER[OFFSET] & 1)
                    if(j < 7):
                        b = (b << 1) & (2 ** 8 - 1)
                        OFFSET += INTERVAL
            
                bits.append(b)
                OFFSET += INTERVAL
            
            else:
                return HIDDEN

#Main function                 
def steg(ACTION, METHOD, INTERVAL, OFFSET, WRAPPER):
    #For retrieval
    if(ACTION == '-r'):
	if(METHOD == '-B'):
	    stdout.write(retreiveByte(INTERVAL, OFFSET, WRAPPER))
	if(METHOD == '-b'):
	    stdout.write(retreiveBit(INTERVAL, OFFSET, WRAPPER))

    #For storage
    if(ACTION == '-s'):
	if(METHOD == '-B'):
	    stdout.write(storeByte(INTERVAL, OFFSET, WRAPPER))
	if(METHOD == '-b'):
	    stdout.write(storeBit(INTERVAL, OFFSET, WRAPPER))

################ ARGUMENTS ##################           
#Action: store or retrieve (s/r)
ACTION = argv[1]

#Method: bit or byte (b/B)
METHOD = argv[2]

#Set offset to <val>
OFFSET = int(argv[3][2:])
if (OFFSET == ''):
    #Default to 0 if none specified
    OFFSET = 0

# checks if there is an interval and if so, get its value
if(argv[4][:2] == '-i'):
    INTERVAL = int(argv[4][2:])
    #Grab the wrapper file, read as binary data, throw an error if one is not specified
    try:
        WRAPPER = open(argv[5][2:], 'rb').read()
        WRAPPER = bytearray(WRAPPER)
    except:
        print "Wrapper file not found, please check your arguments"
else:
    INTERVAL = 1
    #Grab the wrapper file, read as binary data, throw an error if one is not specified
    try:
        WRAPPER = open(argv[4][2:], 'rb').read()
        WRAPPER = bytearray(WRAPPER)
    except:
        print "Wrapper file not found, please check your arguments"


################## Steg ######################
steg(ACTION, METHOD, INTERVAL, OFFSET, WRAPPER)
