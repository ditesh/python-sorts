# Implementation of insertion sort in python
# Ditesh Shashikant Gathani 2010

import support

def sort(data):

	j=1
	outsideLoopCount=0
	swapCount=0
	length = len(data)

	while j <= length -1:
		
		k = 0
		outsideLoopCount += 1

		while k < j:

			if data[k] > data[j]:
				data = support.swap(data, k, j)
				swapCount += 1

			k += 1

		j += 1

#	print "Outside loop count: ", outsideLoopCount
#	print "Swap count: ", swapCount 
	return data

def getName():
	return "insertion"
