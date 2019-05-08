# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUTHOR: Delia Fano Yela
# DATE:  December 2018
# CONTACT: d.fanoyela@qmul.ac.uk
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
# For broadcasting
import numpy as np
# For reading the speech wav files
from scipy.io import wavfile

# ------------------------------------------------------------------------------
# TYPES OF SERIES
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
# COMPUTATION TIME OF VISIBILITY GRAPH FOR DIFFERENT SERIES
# ------------------------------------------------------------------------------
# LENGTH OF SERIES:
# -----------------
L = 1000

# PICK A SERIES:
# -----------------
# Uncomment series you want to use or load your own one

# Balanced tree:
#s = [1,9,2,13,3,10,4,15,5,11,6,14,7,12,8]
#L = len(s)

# Random series
s =  [random.random() for _ in range(L)]

# Random walk
#s = randomwalk(L)
#print s

# Conway series from DC paper
#a = conway(L)
#t = xrange(L)
#b = np.array([a.items()[x][1] for x in t]) - np.array(t)/2
#s = b.tolist()

# Speech example
# fs, data = wavfile.read('./speechexample.wav')
# s0 = data.tolist()
# s = s0[:L]
#L = len(s)
#print "New L : %d" %L
# Set values of the x axis (e.g. time, frequency.. )
timeLine =  range(L) # timeLine contains the 'time stamps' or indexes of the series, the default is set to range

# METHODS:
# --------

#"--------------------------------------"
#" HORIZONTAL VISIBILITY GRAPH"
#"--------------------------------------"
#"BASIC HVG ALGORITHM:"
start = time.time()
out = hvg(s, timeLine)
end = time.time()
print "Basic HVG algorithm : %0.5f seconds" %(end - start)
AdjH = np.zeros((len(s), len(s)))
for el in out:
    AdjH[el] = 1
    AdjH[el[-1::-1]] = 1

#"DIVIDE AND CONQUER HVG ALGORITHM:"
start = time.time()
out = hvg_dc(s, timeLine, 0, L)
end = time.time()
print "Divide&Conquer HVG algorithm : %0.5f seconds" %(end - start)
AdjDCH = np.zeros((len(s), len(s)))
for el in out:
    AdjDCH[el] = 1
    AdjDCH[el[-1::-1]] = 1

#"PROPOSED HVG ALGORITHM:"
start = time.time()
out = visibility(s, timeLine, type = 'horizontal')
end = time.time()
print "Proposed HVG algorithm : %0.5f seconds" %(end - start)
AdjBTH = np.zeros((len(s), len(s)))
for el in out:
    AdjBTH[el] = 1
    AdjBTH[el[-1::-1]] = 1

print "The difference between Adj normal and proposed : %d" % np.sum(AdjH - AdjBTH)
print "The difference between ADj DC and proposed : %d" % np.sum(AdjDCH - AdjBTH)



#"--------------------------------------"
#" NATURAL VISIBILITY GRAPH"
#"--------------------------------------"
#"BASIC NVG ALGORITHM:"
start = time.time()
out = nvg(s, timeLine)
end = time.time()
print "Basic NVG algorithm : %0.5f seconds" %(end - start)
AdjN = np.zeros((len(s), len(s)))
for el in out:
    AdjN[el] = 1
    AdjN[el[-1::-1]] = 1

#"DIVIDE AND CONQUER NVG ALGORITHM:"
timeLine =  range(L) # timeLine contains the 'time stamps' or indexes of the series, the default is set to range
start = time.time()
out = nvg_dc(s, timeLine, 0, L)
end = time.time()
print "Divide&Conquer NVG algorithm : %0.5f seconds" %(end - start)
AdjDCN = np.zeros((len(s), len(s)))
for el in out:
    AdjDCN[el] = 1
    AdjDCN[el[-1::-1]] = 1

#"PROPOSED NVG ALGORITHM:"
start = time.time()
out = visibility(s, type = 'natural')
end = time.time()
print "Proposed NVG algorithm : %0.5f seconds" %(end - start)
AdjBTN = np.zeros((len(s), len(s)))
for el in out:
    AdjBTN[el] = 1
    AdjBTN[el[-1::-1]] = 1

print "The difference between Adj normal and proposed : %d" % np.sum(AdjN - AdjBTN)
print "The difference between Adj DC and proposed : %d" % np.sum(AdjDCN - AdjBTN)
