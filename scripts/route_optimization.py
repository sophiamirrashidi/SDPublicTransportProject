# -*- coding: utf-8 -*-
from __future__ import print_function
import math
import random
import numpy as np
from collections import defaultdict
from simanneal import Annealer
import csv
import latlong.csv
from pyproj import Geod


def mhdist(a, b):
    """Calculates distance between two latitude-longitude coordinates."""
    lat1 = a[0]
    lng1 = a[1]
    lat2 = b[0]
    lng2 = b[1]
    g = Geod(ellps='clrk66')

    gc1 = g.inv(lons1=lng1, lats1=lat1, lons2=lng2, lats2=lat1)
    gc2 = g.inv(lng2, lat1, lng2, lat2)

    mhdist = gc1[2] + gc2[2]

    return mhdist


class TravellingSalesmanProblem(Annealer):

    """Test annealer with a travelling salesman problem.
    """

    # pass extra data (the distance matrix) into the constructor
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TravellingSalesmanProblem, self).__init__(state)  # important!

    def move(self):
        """Swaps two cities in the route."""
        # no efficiency gain, just proof of concept
        # demonstrates returning the delta energy (optional)
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

    cities = {}

    with open('latlong.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')
        linecount = 0
        for row in csvreader:
            if linecount > 78:
                break
            else:
                k = row[0]
                v = (float(row[1]), float(row[2]))
                cities[k] = v
            linecount += 1
        print(f'Processed {linecount} lines.')

  #  print(cities)

    # initial state, a randomly-ordered itinerary
    init_state = list(cities)
    random.shuffle(init_state)

    # create a distance matrix
    distance_matrix = defaultdict(dict)
    for ka, va in cities.items():
        for kb, vb in cities.items():
            distance_matrix[ka][kb] = 0.0 if kb == ka else mhdist(va, vb)

    tsp = TravellingSalesmanProblem(init_state, distance_matrix)
    tsp.set_schedule(tsp.auto(minutes=0.2))
    # since our state is just a list, slice is the fastest way to copy
    tsp.copy_strategy = "slice"
    state, e = tsp.anneal()

    while state[0] != '12804':
        state = state[1:] + state[:1]  # rotate NYC to start

    print()
    print("%i mile route:" % e)
    print(" ➞  ".join(state))


    previousCoordinate = None
    for stop in state:
        coordinate = cities[stop]
        lat = coordinate[0]
        lon = coordinate[1]

        if (previousCoordinate == None):
            print(f"({lat},{lon}),")
        else:
            prevLat = previousCoordinate[0]
            print(f"({prevLat},{lon}),")
            print(f"({lat},{lon}),")
        previousCoordinate = coordinate







            
