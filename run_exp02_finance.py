import csv
import os
# For the methods :
from visibility_algorithms import *
from node_class import *
# For the data generation:
import random
# For performance measurement:
import time

dir = 'DATA/year_2013_fine/' # <------- Change directory to where the finance data is
L = 5000 # Length of series

it = 0

file = open("finance.txt", "a+") # Open file to write results on
file.write('"Type","Computation Time (s)","Visibility","Method"\n ' )


results={
    't_nvg' : [],
    't_dc_nvg' : [],
    't_bt_nvg' : [],
    't_hvg' : [],
    't_dc_hvg' : [],
    't_bt_hvg' : []
}

for filename in os.listdir(dir):

    if it < 100:

        with open(os.path.join(dir, filename)) as csvfile:
            reader = csv.reader(csvfile)
            out = list(reader)

        out2 = []
        for item in out:
            out2.append(float(item[0]))

        print it

        s = out2[:L]

        #"--------------------------------------"
        #" NATURAL VISIBILITY GRAPH"
        #"--------------------------------------"
        #"NVG:"
        timeLine = range(L)
        start = time.time()
        out = nvg(s, timeLine)
        end1 = time.time()

        results['t_nvg'].append(end1 - start)


        #"DC NVG:"
        start = time.time()
        out = nvg_dc(s, timeLine, 0, L)
        end1 = time.time()

        results['t_dc_nvg'].append(end1 - start)


        #"Binary NVG:"
        start = time.time()
        out = visibility(s, timeLine, type = 'natural')
        end1 = time.time()

        results['t_bt_nvg'].append(end1 - start)

        #"--------------------------------------"
        #" HORIZONTAL VISIBILITY GRAPH"
        #"--------------------------------------"

        #"HVG:"
        start = time.time()
        out = hvg(s, timeLine)
        end1 = time.time()

        results['t_hvg'].append(end1 - start)


        #"DC HVG:"
        start = time.time()
        out = hvg_dc(s, timeLine, 0, L)
        end1 = time.time()

        results['t_dc_hvg'].append(end1 - start)

        #"Binary HVG:"
        start = time.time()
        out = visibility(s)
        end1 = time.time()

        results['t_bt_hvg'].append(end1 - start)

        # -------------------------------------------------------------------------
        # WRITE RESULTS IN FILE CSV STYLE
        # -------------------------------------------------------------------------

        file.write('"finance",')
        file.write("%.5f," %results['t_nvg'][it])
        file.write('"nvg",')
        file.write('"basic"\n')

        file.write('"finance",')
        file.write("%.5f," %results['t_dc_nvg'][it])
        file.write('"nvg",')
        file.write('"dc"\n')

        file.write('"finance",')
        file.write("%.5f," %results['t_bt_nvg'][it])
        file.write('"nvg",')
        file.write('"bt"\n')

        file.write('"finance",')
        file.write("%.5f," %results['t_hvg'][it])
        file.write('"hvg",')
        file.write('"basic"\n')

        file.write('"finance",')
        file.write("%.5f," %results['t_dc_hvg'][it])
        file.write('"hvg",')
        file.write('"dc"\n')

        file.write('"finance",')
        file.write("%.5f," %results['t_bt_hvg'][it])
        file.write('"hvg",')
        file.write('"bt"\n')


        it += 1



file.close()


# Save the results dictionary back-up
f = open("dict_finance.txt","w")
f.write( str(results) )
f.close()
