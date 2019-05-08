# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUTHOR: Delia Fano Yela
# DATE:  May 2018
# CONTACT: d.fanoyela@qmul.ac.uk
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Script to test different series and save the different
# visibility algorithms computation times
# ------------------------------------------------------------------------------
# IMPORT
# ------------------------------------------------------------------------------
# For the methods :
from visibility_algorithms import *
from node_class import *
# For the data generation:
import random
# For performance measurement:
import time


# ------------------------------------------------------------------------------
# RECURSION LIMIT
# ------------------------------------------------------------------------------
import sys
# sys.setrecursionlimit(1500) # You might need this for DC algorithm

# ------------------------------------------------------------------------------
# SERIES
# ------------------------------------------------------------------------------
def randomwalk(N):
    # N : size of the series to be generated
    out = [-1 if random.random()<0.5 else 1]
    while(len(out) < N):
        out += [out[-1] + (-1 if random.random()<0.5 else 1 )]
    return out


def conway(N):
    A = {1: 1, 2: 1}
    c = 1 #counter
    while N not in A.keys():
        if c not in A.keys():
            A[c] = A[A[c-1]] + A[c-A[c-1]]
        c += 1
    return A



# ------------------------------------------------------------------------------
# INITS
# ------------------------------------------------------------------------------
S = 10 # number of series for each length to be averaged

all_series = ['walk', 'random','conway']

file = open("results_exp01.txt", "a+") # Open file to write results on
file.write('"computation_time","series_size","series_type","visibility","Method"\n ' )

for L in [10, 50, 1e2, 5e2, 1e3, 5e3, 1e4]:
    print "L : ", L
    L = int(L)

    # ------------------------------------------------------------------------------
    # COMPUTATION TIME GRAPH FOR DIFFERENT SERIES
    # ------------------------------------------------------------------------------

    for series_type in all_series:

        # Conway series
        if series_type == 'conway':
            a = conway(L)
            t = xrange(L)
            b = np.array([a.items()[x][1] for x in t]) - np.array(t)/2
            s = b.tolist()
            S = 1 # the conway series will always take the same values, no point in repeating it
        else:
            S = 10


        for times in xrange(S):

            if series_type == 'random':
                # Random series
                s =  [random.random() for _ in range(L)]
            elif series_type == 'walk':
                # Random walk
                s = randomwalk(L)
            elif series_type == 'conway':
                print "Only computing it once"
            else:
                print " Pick a valid series type: random, walk or conway"


            #"--------------------------------------"
            #" NATURAL VISIBILITY GRAPH"
            #"--------------------------------------"
            timeLine = range(L)
            #"NVG:"
            start = time.time()
            out = nvg(s, timeLine)
            end1 = time.time()

            file.write("%.5f," %(end1 - start))
            file.write("%.5f," %L)
            file.write('"%s",' %series_type)
            file.write('"nvg",')
            file.write('"basic"\n')


            #"DC NVG:"
            start = time.time()
            out = nvg_dc(s, timeLine, 0, L)
            end1 = time.time()

            file.write("%.5f," %(end1 - start))
            file.write("%.5f," %L)
            file.write('"%s",' %series_type)
            file.write('"nvg",')
            file.write('"dc"\n')


            #"Binary NVG:"
            start = time.time()
            out = visibility(s, timeLine, type = 'natural')
            end1 = time.time()

            file.write("%.5f," %(end1 - start))
            file.write("%.5f," %L)
            file.write('"%s",' %series_type)
            file.write('"nvg",')
            file.write('"bt"\n')

            #"--------------------------------------"
            #" HORIZONTAL VISIBILITY GRAPH"
            #"--------------------------------------"

            #"HVG:"
            start = time.time()
            out = hvg(s, timeLine)
            end1 = time.time()

            file.write("%.5f," %(end1 - start))
            file.write("%.5f," %L)
            file.write('"%s",' %series_type)
            file.write('"hvg",')
            file.write('"basic"\n')


            #"DC HVG:"
            start = time.time()
            out = hvg_dc(s, timeLine, 0, L)
            end1 = time.time()

            file.write("%.5f," %(end1 - start))
            file.write("%.5f," %L)
            file.write('"%s",' %series_type)
            file.write('"hvg",')
            file.write('"dc"\n')

            #"Binary HVG:"
            start = time.time()
            out = visibility(s)
            end1 = time.time()

            file.write("%.5f," %(end1 - start))
            file.write("%.5f," %L)
            file.write('"%s",' %series_type)
            file.write('"hvg",')
            file.write('"bt"\n')



file.close()
