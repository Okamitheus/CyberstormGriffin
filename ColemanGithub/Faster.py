########################
# Name: Coleman Levy
# Date: 4/1/2020
# Description: a program in Python 2 that decodes a hidden message from
#              an FTP covert server
########################

#Note: IP, port, folder, and method below can be changed to suit
#whatever situation necessary (ex: change IP from localhost to 
#jeangourd.com to reach his server instead)

from ftplib import FTP

#IP of the FTP trying to be contacted
IP = "138.47.102.67"
#The port being accessed
port = 54321
#The folder being accessed to find files
folder = ""
#7 or 10 method which chooses how many permissions are
#read to create the binary string
METHOD = 10
#Array that will hold the files
files = []
#String later put into the decoder
inputstr = ""
#Output string
text = ""

#Function that reads the permissions and turns them into a binary string
def bitup(files, method):
    #If method is 7 bit...
    if (method == 7):
        #...then skip the first 3 letters in the permissions
        i = 3
    #Otherwise, if the method is 10 bit...
    elif (method == 10):
        #Start at the beginning of the permissions
        i = 0
    #If neither...
    else:
        #Exit with an instructional message
        print "Method must be 7 or 10"
        exit(0)
    #The string that will be returned
    byte = ""
    #For each file in the folder...
    for row in files:
        #..read only the first 10 characters (the permissions)...
        while (i < 10):
            #And if the permission is a dash, add a 0 to the binary
            #string
            if (row[i] == '-'):
                byte += "0"
            #Otherwise, if it has a permission (rwx), then add a 1
            #to the binary string
            else:
                byte += "1"
            #Move to the next character
            i += 1
        #If method is 7, then skip first 3 characters
        if (method == 7):
            i = 3
        #Otherwise, start at the beginning
        else:
            i = 0
    #Return binary string
    return byte

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

#Try to connect to the FTP server
try:
    #The ftp instance
    ftp = FTP()
    #Connect to the server at the specified port
    ftp.connect(IP, port)
    #Login as anonymous (or input username and password to login as user)
    ftp.login("valkyrie", "chooseroftheslain")
    #Move to the folder with the FTP files
    ftp.cwd(folder)
    #Append all the files' info to a string
    ftp.dir(files.append)
    #Exit the server
    ftp.quit()
#If this fails...
except:
    #Exit with an instructional message
    print "FTP connection failed, make sure details are correct"
    exit(0)

#Turn file permissions into binary and save it to this string
inputstr = bitup(files, METHOD)

#...decode the binary as a 7-bit string
text = decode(inputstr, 7)
#Print that the binary is 7-bit and print what it was decoded as
print "7-bit"
print text

if (len(inputstr) % 8 == 0):
#...decode the binary as a 7-bit string
text = decode(inputstr, 8)
#Print that the binary is 8-bit and print what it was decoded as
print "8-bit"
print text
