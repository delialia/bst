# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUTHOR: Delia Fano Yela
# DATE:  December 2018
# CONTACT: d.fanoyela@qmul.ac.uk
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Script to test the trade-off of using the proposed merge function instead
# of recalculating the visibility graph from scratch measured in terms of
# computation time of a random time series.
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


for N in [10,100, int(1e3)]: #, int(1e4)]:
    # Lists initialisations for table representation:
    sizeratio   = []
    sizeL  = []
    timeappend  = []
    isappend    = []
    timeinsert  = []
    isinsert    = []

    # List 'to be appended' (s02)
    s02 = [random.random() for _ in range(N)]

    for j in range(10):
        for L in [N, N*10, N*100, N*1000]:#, int(1e5), int(1e6), int(1e7)]:
            # --------------------------------------------------------------------------
            # Size
            # --------------------------------------------------------------------------
            #sizeratio.append(float(L))
            sizeratio.append(float(L)/float(N))
            # --------------------------------------------------------------------------
            # Series
            # --------------------------------------------------------------------------
            s01  = [random.random() for _ in range(L)]
            # --------------------------------------------------------------------------
            # Append
            # --------------------------------------------------------------------------
            r01 = build(s01, timeLine = range(L))

            s03 = s01 + s02
            t01 = time.time()
            r03 = build(s03, timeLine = range(L+N))
            t02 = time.time()
            r02 = build(s02, timeLine = range(L, L+N))
            rout = merge([r01,r02])
            t03 = time.time()

            timeappend.append(float("{0:.2f}".format((t02-t01)/(t03-t02))))
            isappend.append(isEqual(rout,r03))
            # --------------------------------------------------------------------------
            # Insert
            # --------------------------------------------------------------------------
            step01 = L/5
            step02 = N/5

            s03 = s01[:step01] + s02[:step02]+ s01[step01:2*step01] + s02[step02: 2*step02]+ s01[2*step01:3*step01] + s02[2*step02: 3*step02]+ s01[3*step01:4*step01] + s02[3*step02: 4*step02]+ s01[4*step01:] + s02[4*step02:]
            t03 = range(len(s03))

            t01 = t03[:step01]+ t03[step01+step02 : 2*step01 +step02] + t03[2*step01+2*step02 : 3*step01 +2*step02] + t03[3*step01+3*step02 : 4*step01 +3*step02] + t03[4*step01+4*step02 : 5*step01 +4*step02]
            tm02 = t03[step01: step01+step02] + t03[2*step01+step02: 2*step01+2*step02]+ t03[3*step01+2*step02: 3*step01+3*step02] + t03[4*step01+3*step02: 4*step01+4*step02] + t03[5*step01+4*step02: 5*step01+5*step02]

            r01 = build(s01, timeLine = t01)
            #r02 = build(s02, timeLine = t02)

            t01 = time.time()
            r03 = build(s03, timeLine = t03)
            t02 = time.time()
            r02 = build(s02, timeLine = tm02)
            rout = merge([r01, r02])
            t03 = time.time()

            timeinsert.append(float("{0:.2f}".format((t02-t01)/(t03-t02))))
            isinsert.append(isEqual(rout,r03))



    # -------------------------------------------------------------------------
    # WRITE RESULTS IN FILE CSV STYLE
    # -------------------------------------------------------------------------
    file = open("merge.txt", "a+") # Open file to write results on

    file.write('"N","size ratio","time ratio","type"\n' )
    for i in xrange(len(sizeratio)):
        file.write("%i," %N)
        file.write("%.5f," %sizeratio[i])
        file.write("%.5f," %timeappend[i])
        file.write('"Append"\n')

        file.write("%i," %N)
        file.write("%.5f," %sizeratio[i])
        file.write("%.5f," %timeinsert[i])
        file.write('"Insert"\n')

    file.close()

    print isappend
    print isinsert
