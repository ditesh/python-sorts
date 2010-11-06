#!/usr/bin/env python
# Implementations of common sorts
# Ditesh Shashikant Gathani (c) 2010

import sys
import support

def main(argv=None):

	sorts = ["merge", "quick", "bubble", "selection", "insertion"]

        if argv is None:
                argv = sys.argv

	if len(argv) != 3:
		print >> sys.stderr, "Invalid argument list - specify type of sort and data size"
		sys.exit(1)

	sortType = argv[1]
	dataSize = argv[2]

	if sortType not in sorts and sortType != "all":
		print >> sys.stderr, "Invalid sort specified, valid sorts are:"
		print >> sys.stderr, sorts
		sys.exit(1)

	if not dataSize.isdigit():
		print >> sys.stderr, "Invalid sort size specified, valid size is a positive integer"
		sys.exit(1)

	dataSize = int(dataSize)

	if dataSize <= 0:
		print >> sys.stderr, "Invalid sort size specified, valid size is a positive integer"
		sys.exit(1)

	data = support.getDataSource(dataSize)

	if sortType == "all":
		for type in sorts:
			support.startTiming()
			sorter = __import__(type)
			print "Using", sorter.getName(), "sort"
			sortedData = sorter.sort(data)
			printData(data, sortedData);

	else:
		support.startTiming()
		sorter = __import__(sortType)
		print "Using", sorter.getName(), "sort"
		sortedData = sorter.sort(data)
		printData(data, sortedData);


def printData(data, sortedData):

#	print "Sorted data: ", sortedData
	print "Time taken: ", support.endTiming(), "(s)"

	correctLength = support.checkLength(data, sortedData)
	sorted = support.checkSorted(sortedData)

	if correctLength is False:
		print "Correct length: ", correctLength

	if sorted is False:
		print "Sorted: ", sorted

	print

	

if __name__ == "__main__":
	sys.exit(main())
