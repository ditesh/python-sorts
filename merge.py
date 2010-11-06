# Implementation of merge sort in python
# Ditesh Shashikant Gathani 2010

import support

def sort(data):

	length = len(data)

	if length == 1:
		return data

	midpoint = length/2

	left = data[:midpoint]
	right = data[midpoint:]

	left = sort(left)
	right = sort(right)

	return merge(left, right)

def merge(left, right):

	i = 0
	rIndex = 0
	lIndex = 0
	returnValue = []
	leftLength = len(left)
	rightLength = len(right)

	while i < leftLength + rightLength:

		if lIndex < leftLength and rIndex < rightLength:

			if left[lIndex] == right[rIndex]:
				returnValue.append(left[lIndex])
				returnValue.append(right[rIndex])
				lIndex += 1
				rIndex += 1

			elif left[lIndex] < right[rIndex]:
				returnValue.append(left[lIndex])
				lIndex += 1

			elif right[rIndex] < left[lIndex]:
				returnValue.append(right[rIndex])
				rIndex += 1

		elif lIndex <= leftLength-1:
			returnValue += left[lIndex:]
			break

		elif rIndex <= rightLength-1:
			returnValue += right[rIndex:]
			break

		i += 1

	return returnValue

def getName():
	return "merge"
