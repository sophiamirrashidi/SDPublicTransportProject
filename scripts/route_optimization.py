import math
import random
import numpy as np
from collections import defaultdict
from simanneal import Annealer
import csv
from pyproj import Geod


def mhdist(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    lat1 = a[0]
    lng1 = a[1]
    lat2 = b[0]
    lng2 = b[1]
    g = Geod(ellps='clrk66') #initialize a Geod to perform geodesic calculations for MH distance

    gc1 = g.inv(lons1=lng1, lats1=lat1, lons2=lng2, lats2=lat1) # calculate East-West distance
    gc2 = g.inv(lng2, lat1, lng2, lat2) # calculate North-South distance

    mhdist = gc1[2] + gc2[2] # add together to get MH distance

    return mhdist


class TravellingSalesmanProblem(Annealer):

    """Uses the annealer from simmaneal to find the optimal route between bus stops
    
    """

    # pass the distance matrix into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two stops in the route."""
        initial_energy = self.energy()

        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

        return self.energy() - initial_energy

    def energy(self):
        """Calculates the length of the route."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e


if __name__ == '__main__':

    stops = {}

    # read in stop data 
    
    with open('latlong.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        linecount = 0
        for row in csvreader:
            if linecount > 78: # 78 total stops
                break
            else:
                k = row[0]
                v = (float(row[1]), float(row[2]))
                stops[k] = v
            linecount += 1
        print(f'Processed {linecount} lines.')


    # initial state list contains tuples of stop_id, latitude, longitude from the stops dictionary
    init_state = list(stops)  
    random.shuffle(init_state) # shuffle initial state
 
    """
    create distance matrix: nested dictionary structure; key is a stop; 
    value is a dictionary with key being all other stops, values being distances to stops 
    """
    
    distance_matrix = defaultdict(dict) 
    for ka, va in stops.items():
        for kb, vb in stops.items():
            distance_matrix[ka][kb] = 0.0 if kb == ka else mhdist(va, vb)

    tsp = TravellingSalesmanProblem(init_state, distance_matrix) # initialize TSP with randomized state and the generated distance matrix
    tsp.set_schedule(tsp.auto(minutes=0.2)) # decrease temp every 0.2 minutes 
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal() # perform simulated annealing

    while state[0] != '12804':  # start from stop 12804
        state = state[1:] + state[:1] 

    # print solution 
    
    print()
    print("%i mile route:" % e)
    print(" ➞  ".join(state))


    previousCoordinate = None
    for stop in state:
        coordinate = stops[stop]
        lat = coordinate[0]
        lon = coordinate[1]

        if (previousCoordinate == None):
            print(f"({lat},{lon}),")
        else:
            prevLat = previousCoordinate[0]
            print(f"({prevLat},{lon}),")
            print(f"({lat},{lon}),")
        previousCoordinate = coordinate







            
