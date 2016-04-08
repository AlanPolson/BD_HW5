#!/usr/bin/env python
import sys, time

def parseRecords():
    for line in sys.stdin:
    	line = line.strip('\n')
    	line = line.split(',')
        yield int(line[2])/60

def mapper():
	mins = {}
	for tripdur in parseRecords():
		mins[tripdur]=mins.get(tripdur,0)+1
    	print '%s\t%s' % (0,mins)

if __name__=='__main__':
    mapper()