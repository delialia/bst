import csv
import os
# For the methods :
from visibility_algorithms import *
from node_class import *
# For the data generation:
import random
# For performance measurement:
import time
# For reading the speech wav files
from scipy.io import wavfile
# Wav conversion
from scikits.audiolab import Format, Sndfile

# Get paths for the wav files
src_dir = 'DATA/TRAIN/' # <------- Change directory to where the finance data is

paths_timit = []

for subdir, dirs, files in os.walk(src_dir):
    for filename in files:
        if filename[-3:] == 'WAV':
            paths_timit.append(os.path.join(subdir, filename))

#print paths_timit
print len(paths_timit)

paths_timit_totest = paths_timit[:100]
print len(paths_timit_totest)

file = open("speech.txt", "a+") # Open file to write results on
file.write('"Type","Computation Time (s)","Visibility","Method"\n ' )

L = 5000

i = 0


results={
    't_nvg' : [],
    't_dc_nvg' : [],
    't_bt_nvg' : [],
    't_hvg' : [],
    't_dc_hvg' : [],
    't_bt_hvg' : []
}

for filename in paths_timit_totest:

    print i
    print filename

    try:
        (rate,sig)= wavfile.read(filename)
    except ValueError as e:
        if e.message == "File format 'NIST'... not understood.":
            ss = Sndfile(filename, 'r')
            nframes = ss.nframes
            sig = ss.read_frames(nframes)
            rate = ss.samplerate


    data = sig.tolist()
    s = data[3000:(3000+L)]


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

    #"--------------------------------------"
    #" WRITE RESULTS
    #"--------------------------------------"
    file.write('"speech",')
    file.write("%.5f," %results['t_nvg'][i])
    file.write('"nvg",')
    file.write('"basic"\n')

    file.write('"speech",')
    file.write("%.5f," %results['t_dc_nvg'][i])
    file.write('"nvg",')
    file.write('"dc"\n')

    file.write('"speech",')
    file.write("%.5f," %results['t_bt_nvg'][i])
    file.write('"nvg",')
    file.write('"bt"\n')

    file.write('"speech",')
    file.write("%.5f," %results['t_hvg'][i])
    file.write('"hvg",')
    file.write('"basic"\n')

    file.write('"speech",')
    file.write("%.5f," %results['t_dc_hvg'][i])
    file.write('"hvg",')
    file.write('"dc"\n')

    file.write('"speech",')
    file.write("%.5f," %results['t_bt_hvg'][i])
    file.write('"hvg",')
    file.write('"bt"\n')

    i += 1


file.close()



# Save the results dictionary back-up
f = open("dict_speech.txt","w")
f.write( str(results) )
f.close()
