import math
import random
from simanneal import Annealer
import csv
from stop import *

stoplist = []

with open('data/updatedstops.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        linecount = 0
        for row in csvreader:
            if linecount == 0:
                print(f'Column names are {", ".join(row)}')
                linecount += 1
                continue
            if linecount > 78:
                break
            else:
                stop = Stop(row[0], row[1], row[2], row[3], row[6], row[10], row[11])
                stoplist.append(stop)                
            linecount += 1
        print(f'Processed {linecount} lines.')

for stop in stoplist:
    print(stop.getImportance())


depmax = 725
depmin = 160
deprng = depmax - depmin

minimp = 0.0007167554416
maximp = 0.1049084495
imprng = maximp - minimp


for stop in stoplist:
    val = (float(stop.getImportance()) - minimp)/imprng
    numdep = depmin + val * deprng
    print(f'StopId = {stop.getStopid()}, dep = {numdep}')

