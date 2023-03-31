from __future__ import print_function
import math
import random
from collections import defaultdict
from simanneal import Annealer
import csv
from stop import *

#class StopOp(Annealer):

#    def move(self):

#   def energy(self):
    



if __name__ == "__main__":
     
    stoplist = []

    with open('data/stops.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        linecount = 0
        for row in csvreader:
            if linecount == 0:
                print(f'Column names are {", ".join(row)}')
            else:
                stop = Stop(row[0], row[1], row[2], row[3], row[4])
                stoplist.append(stop)                
            linecount += 1
        print(f'Processed {linecount} lines.')

        total = 0
        maximum = 0
        for stop in stoplist:
            weight = stop.getWeight()
#            print(f'weight: {weight}')
            if weight > maximum:
                maximum = weight
            total += weight

        print(f'total: {total}, max: {maximum}')


        for stop in stoplist:
            weight = stop.getWeight()
            imp = (maximum - weight)/(total)
            stop.setImportance(imp)
            print(stop)




            
                
    
