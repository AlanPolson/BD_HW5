#!/usr/bin/env python
import sys, time

def parseRecords():
    for line in sys.stdin:
    	line = line.strip('\n')
    	line = line.split()
        yield line[2]

def mapper():
    for trips in parseRecords():
    	print '%s\t%s' % ((int(trips)/60),1)

if __name__=='__main__':
    mapper()