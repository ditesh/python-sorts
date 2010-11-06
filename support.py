# Support library

import random
import time

# Not the best practice, but it suffices for our needs
startTime = 0
endTime = 0

# Returns a list of random numbers
def getDataSource(x=1000000):
	data = range(0,x)
	random.shuffle(data)
	return data

def swap(data, i, j):
	x = data[j]
	data[j] = data[i]
	data[i] = x
	return data

def checkSorted(data):

	j = data[0]

	for i in data[1:]:

		if (i-j) == 1:
			j = i
			continue
		else:
			return False

	return True

def startTiming():
	global startTime
	startTime = time.time()

def endTiming():
	global startTime, endTime
	endTime = time.time()
	return endTime - startTime

def checkLength(x, y):

	if len(x) != len(y):
		return False

	return True
