from __future__ import print_function
import math
import random
from collections import defaultdict
from simanneal import Annealer
import csv
from stop import *

class StopOp(Annealer):

    def __init__(self, stoplist):
        self.stoplist = stoplist
        super(StopOp, self).__init__(stoplist)  # important!
        
    def move(self):
        initial_energy = self.energy()

        a = random.randint(0, len(self.stoplist) - 1)
        b = random.randint(0, 9)
        freq = stoplist[a].getFreq()

        if(freq < 3):
            pass
        elif(freq > 8):
            pass
        elif(b > 5):
            stoplist[a].setFreq(freq+1)
        else:
            stoplist[a].setFreq(freq-1)
        print(f'a: {a}, b: {b}, freq: {freq}, newFreq: {stoplist[a].getFreq()}')

        return self.energy() - initial_energy


    def energy(self):
        tot = 0
        for stop in stoplist:
            tot += stop.getImportance()* stop.getFreq()

#        print(tot)

        return tot



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

    stopop = StopOp(stoplist)
    stopop.set_schedule(stopop.auto(minutes=0.2))
    stopop.copy_strategy = "deepcopy"
    finalstate, e = stopop.anneal()

    for stop in finalstate:
        print(stop)


    

    




            
                
    
