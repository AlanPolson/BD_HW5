#!/usr/bin/env python
import itertools, operator, sys

def parsePairs():
    for line in sys.stdin:
        yield tuple(line.strip('\n').split('\t'))

def reducer():
    for key, pairs in itertools.groupby(parsePairs(),
                                        operator.itemgetter(0)):
        count = sum(int(i[1]) for i in pairs)
        print '%s\t%s' % (key, count)
"""
        dic={}
        dic[key]=count



    print "Computing median..."

    total = 0
	for t in d:
	    total += t*d.get(t)
	n = (total+1)/len(d)
	check_med = n
	for t in sorted(d):
	    check_med -=t*d.get(t)
	    if check_med <= 0:
	        print t
	        break


"""
if __name__=='__main__':
    reducer()
