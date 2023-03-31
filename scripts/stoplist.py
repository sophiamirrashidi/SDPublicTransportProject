import csv
import stopobs
     
stoplist = []

with open('/Users/sophia/Downloads/DSPROJECT/data/stops.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    linecount = 1



