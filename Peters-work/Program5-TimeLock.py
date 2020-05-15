#Program5-TimeLock Python 2.7 Peter Ford
#Im not wathing your videos for your view on politics, human interaction is a required part of mental health
import sys
import datetime
import hashlib
import pytz
import math

Debug=False

def readTime():
	try:
		USE_DEFAULT=False;
		default_epoch='2020 05 08 10 00 00'
		#read-in stdin and set epoch if it has a value
		lines=sys.stdin.readlines()
		if(lines == []):
			USE_DEFAULT=True

		#use either default time or user-entered time
		if(USE_DEFAULT):
			epoch=default_epoch
		else:
			epoch=lines[0]
		if (Debug):
			print epoch
		return epoch
	except Exception as e:
		print("the error is:")
		print(e);
		print("enter time in format YYYY MM DD HH mm SS");

def Main():
	interval=60
	#get current and epoch time then caculate the difference as datetime objects for each minute
	datetimeFormat='%Y %m %d %H %M %S'
	local_tz=pytz.timezone('America/Chicago')
	utc_tz=pytz.timezone('UTC')
	#to set current time comment out the line 2 below and use the current time in formatt above
	#current_time='2017 04 23 18 02 30'
	#current_time=datetime.datetime.strptime(current_time, datetimeFormat)
	current_time=datetime.datetime.now().replace(microsecond=0,)
	current_time=local_tz.localize(current_time, is_dst=None)
	current_time=current_time.astimezone(pytz.utc)
	epoch=readTime().rstrip()
	dateTimeEpoch=datetime.datetime.strptime(epoch, datetimeFormat)
	dateTimeEpoch=local_tz.localize(dateTimeEpoch, is_dst=None)
	dateTimeEpoch=dateTimeEpoch.astimezone(pytz.utc)
	timeElapsed=current_time-dateTimeEpoch
	if (Debug):
		print timeElapsed
	#find time elapsed in seconds
	deltaSeconds=timeElapsed.days*86400 + timeElapsed.seconds
	deltaSeconds=deltaSeconds-deltaSeconds%interval
	if(Debug):
		print ("time elapsed in seconds: ")
		print(deltaSeconds)

	#hash it twice
	hashy=hashlib.md5(str(deltaSeconds)).hexdigest().rstrip()
	hashy2=hashlib.md5(str(hashy)).hexdigest()
	if(Debug):
		print hashy +" and "+ hashy2

	#from the hash pull out first two letters and last two numbers
	Key=''
	letters=0
	numbers=0
	i=0
	hashArrary=[]	
	reverseHash=''
	#reverse order of has to get first to numbers right- to - left
	for char in hashy2:
		reverseHash= char+reverseHash
	while(letters<=1):
		for char in hashy2:
			if (char.isalpha()):
				if(Debug):
					print char
				Key+=char
				letters+=1
				if(letters>=2):
					break
	while (numbers<=1):
		for char in reverseHash:
			if not(char.isalpha()):
				if(Debug):
					print char
				Key+=char
				numbers+=1
				if(numbers>=2):
					break
	mid=int(math.floor(len(hashy2)/2))
	Key+=hashy2[mid]
		
	print "the Key is: "+Key
Main()




