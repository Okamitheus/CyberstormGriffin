########################
# Name: Coleman Levy
# Date: 4/11/2020
# Description: a program in Python 3 that creates a password
#              based on the difference between two dates in seconds
########################
from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

#Debug for printing out extra info (not implemented)
DEBUG = True

#Set to true if on the challenge server
On_Server = False

#The interval is set to one minute
INTERVAL = 60

#Manual time to be entered as ending time
Manual_Time = "2020 05 08 11 37 01"

#Strings to hold the MD5 code and the created password
code = ""
password = ""

#The time zone
tz = pytz.timezone('US/Central')

#Function that converts a string with a date in it to
#anm actual datetime variable
def dateUp(time):
    #Try...
    try:
        #The year, month, day, hour, minute, and second are created as ints
        #from the string
        Year = int(time[0:4])
        Month = int(time[5:7])
        Day = int(time[8:10])
        Hour = int(time[11:13])
        Minute = int(time[14:16])
        Second = int(time[17:19])
        #Converts the previous variables into a single datetime variable and returns it
        return datetime(Year, Month, Day, Hour, Minute, Second)
    #If this fails, return message with error to user and quit program
    except:
        print ("You must enter appropriate dates.")
        exit(0)

#The ending datetime variable (created by converting Manual_Time)
ending = datetime.now()
#The beginning datetime variable (created from the input file)
beginning = dateUp(stdin.read().rstrip("\n"))

#Converts both ending and beginning time to the UTC time zone
ending = tz.normalize(tz.localize(ending)).astimezone(pytz.utc)
beginning = tz.normalize(tz.localize(beginning)).astimezone(pytz.utc)

#Print the beginning and ending datetimes
print(beginning)
print(ending)

#Find the difference between beginning and ending datetimes in seconds
delta = int((ending - beginning).total_seconds())
#Print this difference
print (delta)

#Change the number of seconds to fit the 1 minute interval
delta -= (delta % 60)
#Print this new delta
print (delta)

#Convert the delta to MD5 code
code = md5((str(delta)).encode())
code = code.hexdigest()
#Print this code
print (code)

#MD5 encode the code as well
code = md5(code.encode())
code = code.hexdigest()
#Print the double MD5 code
print (code)

#Int for iterations
i = 0
#Iterate through every character in the code (left to right)
while (i < len(code)):
    #If the character isn't a number...
    if (not code[i].isdigit()):
        #Add it to the password
        password += code[i]
        #If two letters have been found, stop looking for more letters
        if (len(password) == 2):
            i = len(code)
    i += 1

#Start iterator at end of code
i = len(code) - 1
#Iterate through every character in the code (right to left)
while (i >= 0):
    #If the character is a number...
    if (code[i].isdigit()):
        #Add it to the password
        password += code[i]
        #If two numbers have been found, stop looking for more numbers
        if (len(password) == 4):
            i = 0
    i -= 1

password += code[len(code)-1]

#Print the password
print (password)
