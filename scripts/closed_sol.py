import math
import random
from simanneal import Annealer
import csv
from stop import *


with open('data/stops.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        linecount = 0
        for row in csvreader:
            if linecount == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                stop = Stop(row[0], row[1], row[2], row[3], row[6], row[10], row[11])
                stoplist.append(stop)                
            linecount += 1
        print(f'Processed {linecount} lines.')
