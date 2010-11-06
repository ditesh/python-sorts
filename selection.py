# Implementation of selection sort in python
# Ditesh Shashikant Gathani 2010

import support

def sort(data):

	j=0
	outsideLoopCount=0
	swapCount=0

	swapped = True 
	length = len(data)

	while j <= length -1:

		k = j + 1
		smallest = data[j]
		outsideLoopCount += 1

		while k <= (length - 1):

			if data[k] < smallest:
				smallIndex = k
				smallest = data[k]

			k += 1

		for l in range(0, j+1):

			if data[l] > smallest:
				data = support.swap(data, l, smallIndex)
				swapCount += 1

		j += 1

#	print "Outside loop count: ", outsideLoopCount
#	print "Swap count: ", swapCount 
	return data

def getName():
	return "selection"
