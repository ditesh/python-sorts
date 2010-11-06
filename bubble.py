# Implementation of bubble sort in python
# Ditesh Shashikant Gathani 2010

import support

def sort(data):

	outsideLoopCount=0
	swapCount=0
	swapped = True 
	length = len(data)

	while swapped:

		j = 0
		outsideLoopCount += 1
		swapped = False

		while j + 1 < length:

			if data[j] > data[j+1]:
				swapCount += 1
				data = support.swap(data, j, j+1)
				swapped = True

			j += 1

#	print "Outside loop count: ", outsideLoopCount
#	print "Swap count: ", swapCount 
	return data

def getName():
	return "bubble"
