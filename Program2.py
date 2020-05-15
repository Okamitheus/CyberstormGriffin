from sys import stdin, argv
'using Python 2.7'

Domain = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(plaintext, key):
	ciphertext = ""
	#make Key sutible for use by putting all valuse from Domain into a string to cycle through
	key = key.upper()
	keyForUse=''
	for letter in key:
		for x in Domain:
			if(letter == x):
				keyForUse+=letter


	keyCounter=0
      	for letter in plaintext:
		#check if valid character to encrypt
		valid = False
		Capital = letter.isupper()
		letter = letter.upper()

		#print keyForUse
		for x in Domain:
			#if valid character throw flag and convert to domain index
			if (letter == x):
				valid = True
				Pi = Domain.index(letter)
				#print "Pi =  " + letter + " = " + str(Pi)

				#if we found a character find the key value and add them
				keyCounter=keyCounter%len(keyForUse)
				keyLetter = keyForUse[keyCounter]
				Ki = Domain.index(keyLetter)
				#print "Ki = " +keyLetter +" = "+str(Ki)
		#valid  characters indexs get added to key indexes and modulused by the Domain
		if (valid):
			index = (Pi + Ki) % len(Domain)
			letter = Domain[index]
			if (not Capital):
				letter = letter.lower()
			ciphertext+=letter
			#print "index = " + str(index) + " = " +letter
		#Invalid characters just get appended
		else:
			ciphertext+=letter

		#only progress the key counter if we found a valid character
		if(valid):
			keyCounter += 1	

	return ciphertext

def decypt(ciphertext, key):
	plaintext = ""
	#make Key sutible for use by putting all valuse from Domain into a string to cycle through
	key = key.upper()
	keyForUse=''
	for letter in key:
		for x in Domain:
			if(letter == x):
				keyForUse+=letter
	keyCounter = 0
	for letter in ciphertext:
		#check if valid character to decryptand find capitilization
		valid = False
		Capital = letter.isupper()
		letter = letter.upper()

		#print keyForUse
		for x in Domain:
			#if valid character throw flag and convert to domain index
			if (letter == x):

				valid = True
				Ci = Domain.index(letter)
				#print "Ci =  " + letter + " = " + str(Ci)

				#if we found a character find the key value and add them
				keyCounter=keyCounter%len(keyForUse)
				keyLetter = keyForUse[keyCounter]
				Ki = Domain.index(keyLetter)
				#print "Ki = " +keyLetter +" = "+str(Ki)
		#valid  characters indexs get added to key indexes and modulused by the Domain
		if (valid):
			index = (Ci - Ki + len(Domain)) % len(Domain)
			letter = Domain[index]
			if (not Capital):
				letter = letter.lower()
			plaintext+=letter
			#print "index = " + str(index) + " = " +letter
		#Invalid characters just get appended
		else:
			plaintext+=letter

		#only progress the key counter if we found a valid character
		if(valid):
			keyCounter += 1	

	return plaintext


try:

	'implement error catching'
	mode = argv[1]
	key = argv[2]

	text = stdin.read().rstrip("\n")

	if (mode == "-e"):
		ciphertext = encrypt(text, key)
		print ciphertext
	elif (mode == "-d"):
		plaintext = decypt(text, key)
		print plaintext
except:
	print "To use this utility use the syntax: '<Program Name> -(options) <Key>' \n options are -e or -d for encrpyt and decrypt respectivly"

