#Katie Hay Timelock Program 5
#4/24/20
#Python 2

from sys import stdin
import datetime
import pytz
import time
from hashlib import md5
import math

#Debug mode
DEBUG = False 

#Manual current datetime
#CURRENT = "2020 05 08 10 00 00"

#System current datetime
CURRENT = datetime.datetime.now()

#Epoch time from stdin
EPOCH = stdin.readline().rstrip("\n")

def timelock(current, epoch):
	#Naive datetime
	nc = current #if using realtime
	#nc = datetime.datetime.strptime(current, "%Y %m %d %H %M %S") #if using manual time
	ne = datetime.datetime.strptime(epoch, "%Y %m %d %H %M %S")
	#timezones
	utc = pytz.timezone('UTC')
	cdt = pytz.timezone('US/Central')
	#localize the naive
	c_utc = cdt.localize(nc, is_dst=None).astimezone(utc)
	e_utc = cdt.localize(ne, is_dst=None).astimezone(utc)
	#Convert dates to seconds and find the difference
	t1 = time.mktime(c_utc.timetuple())
	t2 = time.mktime(e_utc.timetuple())
	delta = int(t1-t2)
	
	#getting into the beginning of the 60 second interval
	while(delta % 60 != 0):
		delta = delta - 1
	
	#convert to string and remove new line char
	delta = str(delta).strip()
	#MD5 1:
	first = md5(delta).hexdigest()
	#MD5 2:
	second = md5(first).hexdigest()
	#print second
	y = int(math.floor(len(second)/2)) -1
	#print y
	#print second[y]
	#getting the first two letters
	letters = ""
	for char in second:
		#comparing ascii values
		if(ord(char) >= 97 and ord(char) <= 122):
			if (len(letters) < 2):
				letters += char

	#getting the last two numbers		
	numbers = ""
	reverse = second[::-1]
	for char in reverse:
		#comparing ascii values
		if(ord(char) >= 48 and ord(char) <= 57):
			if(len(numbers) < 2):
				numbers += char
		
	code = letters + numbers + second[y]

	#debug mode
	if (DEBUG):
                print c_utc
                print e_utc
		print delta
		print first
		print second
		print letters

	print code

timelock(CURRENT, EPOCH)
