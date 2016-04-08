#!/usr/bin/env python
import itertools, operator, sys, ast

def parsePairs():
    for line in sys.stdin:
        yield tuple(line.strip('\n').split('\t'))

def addBins((bins,tot_count),one_chunk_of_min_dicts):
    for (m,c) in one_chunk_of_min_dicts.iteritems():
        bins[m] = bins.get(m,0)+c
        tot_count +=c
    return (bins, tot_count)

# #3
# def reducer():
#     for (now_useless_zero, min_dicts_as_list)
#     #Remember: reduce basically does: addBins( ({},0) , mins_as_list[0] )
#     #                      and then : addBins( returned(bins, tot_count) , mins_as_list[1] ) and so on for the next dictionaries
    
#     (bins, total_count) = reduce(addBins, min_dicts_as_list, ({}, 0))
#     #the above 'bins' now contains a single dictionary, containing all the trip_durs and their frequency, as well as total count (=46200)
#     #We will use this number, below, to calculate the median trip_dur(in mins)
    






def reducer():
    for useless_zero, pairs in itertools.groupby(parsePairs(),
                                        operator.itemgetter(0)):
    #'parse pairs yields five 'pairs' each pairs contains an entire dictionary, but as of now, python reads the '{}' as just string characters
    # the map functions applies the function ast.literal_eval() to all 5 dictionaries in pairs (pairs[0] is just the useless zero)
    # the literal_eval function is kinda like 'eval', except that it doesn't execute any functions that the string may contain. It just reads
    # the string literals as if they are literals.
        (bins, total_count) = reduce(addBins, map(lambda x: ast.literal_eval(x[1]), pairs), ({}, 0))
    #the above 'bins' now contains a single dictionary, containing all the trip_durs and their frequency, as well as total count (=46200)
    #We will use this number, below, to calculate the median trip_dur(in mins)

    count = 0
    for (m,c) in bins.iteritems():
        count+=c
        if count>total_count/2:
            print "The median trip duration is {} minutes" .format(m)
            break
    return '0'

        

if __name__=='__main__':
    reducer()
