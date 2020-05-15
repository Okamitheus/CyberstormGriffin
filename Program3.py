#Peter Ford python2.7
from ftplib import FTP

#Gloabals
IP = 'jeangourd.com'
PORT = 8008
FOLDER = ""
METHOD = 7
DEBUG = 0


#Isolates file permissions and change them to usable binary
def CreateBinaryOfPermissions(contents):
	binary=''
	for row in contents:
		permissions = row[0:10]
		permissions = permissions.replace("-","0")
		permissions = permissions.replace("r","1")
		permissions = permissions.replace("x","1") 
		permissions = permissions.replace("d","1") 
		permissions = permissions.replace("w","1") 
		if (DEBUG):
			print permissions
		binary+=permissions
	return binary

#decode a single character
def decode(binary, n):
	text = ""
	i = 0
	while (i < len(binary)):
		byte = binary[i:i+n]
		byte = int(byte,2)
		'it was 8 not 9  :)'
		if (byte == 8):
			'If backspace remove the last character'
			text = text.rstrip(text[len(text)-1])
		else:
			text += chr(byte)
		i += n
	return text

#decode a string of binary data and print the results
def binaryDecoder(binaryString):
	if(len(binaryString) % 7 == 0):
		text = decode(binaryString, 7)
		print text
	if(len(binaryString) % 8 == 0):
		text = decode(binaryString, 8)
		print text



############# MAIN ####################################################
#logs on, grabs contents from ftp server, and closes the connection
contents=[]
ftp=FTP()
ftp.connect(IP, PORT)
ftp.login()
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

if(DEBUG):
	#display the contents
	for row in contents:
		print row

#turn permmisions to binary
permissions = CreateBinaryOfPermissions(contents)
if(DEBUG):
	print permissions
#now that we can use permissions, decode based off 7 or 10
if(METHOD == 7):
	i=0
	filteredBinary=''
	#sort out which ones start with 000 and feed the new string into the decoder
	while(i<len(permissions)):
		if(permissions[i:i+3]=="000"):
			filteredBinary+=permissions[i+3:i+10]
		i+=10
	binaryDecoder(filteredBinary)
#if we use them all just pass the binary string to the decoder
elif(METHOD ==10):
	binaryDecoder(permissions)



	

