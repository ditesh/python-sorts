# Implementation of quick sort in python
# Ditesh Shashikant Gathani 2010

import sys
import support

def sort(data):

	length = len(data)

	if length <= 1:
		return data

	i = 0
	left = []
	right = []
	pivot, pivotIndex = getPivot(data)

	while i < length:

		if i == pivotIndex:
			i += 1
			continue

		if data[i] <= pivot:
			left.append(data[i])
		else:
			right.append(data[i])

		i += 1

	return sort(left) + [pivot] + sort(right)

def getName():
	return "quick"

def getPivot(data):
	return (data[0], 0)
