#Katie Hay 4/3/20
#Challenge 1: FTP Covert Channel
#Version 2.7.15

from ftplib import FTP

#preferred method
METHOD = 10

#FTP specifics
IP = "jeangourd.com"
PORT = 8008
FOLDER = "/.secretstorage/.folder2/.howaboutonemore"
USE_PASSIVE = True
USER = "valkyrie"
PASS = "chooseroftheslain"

# Contents of the folder
contents = []

# Isolated permissions
perm = []

# 7 and 8-bit binary strings
binary7 = ""
binary8 = ""

# Connecting to the FTP, grabbing the contents, and diconnecting
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASS)
ftp.set_pasv(USE_PASSIVE)
ftp.cwd(FOLDER)
ftp.dir(contents.append)
ftp.quit()

#Binary decoding function
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

#For 7-bit method:
if (METHOD == 7):
    for row in contents:
        # Remove all noise files and add each valuable file permission to perm list
        if (row[0:3] == "---"):
            perm.append(row[3:10])
    #convert permissions to binary and add to binary7 list
    i=0
    while (i < len(perm)):
        j=0
        while (j < len(perm[i])):
            if (perm[i][j] == "-"):
                binary7 += "0"
            else: 
                binary7 += "1"
            j+=1
        i+=1
    #decode the binary number
    print decode(binary7,7)
        
# For 10-bit method: 
if (METHOD == 10):
    #isolate the permissions
    for row in contents:
        perm.append(row[0:10])
    #convert permissions to binary and add to binary list
    i=0
    while (i < len(perm)):
        j=0
        while (j < len(perm[i])):
            if (perm[i][j] == "-"):
                binary7 += "0"
            else: 
                binary7 += "1"
            j+=1
        i+=1
        binary8 = binary7
    
    #if the 7-bit binary number is not able to be grouped in 7 even bits, add fluff
    if (((len(binary7)) % 7) != 0):
        binary7 += "0"

    #if the 8-bit binary number is not able to be grouped in 8 even bits, add fluff
    if (((len(binary8)) % 8) != 0):
        binary8 += "0"

    #print the 7 and 8-bit version of the message, one will be stupid
    print "7-bit: " + decode(binary7,7)
    print "8-bit: " + decode(binary8,8)

