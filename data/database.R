library(DBI)
library(sqldf)
library(RSQLite)
setwd('/Users/sophia/Downloads/DSPROJECT/SDPublicTransportProject/data')
drv = dbDriver('SQLite')
db = dbConnect(drv, dbname = 'gtfsdatabase.sqlite')

routes = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/routes.txt')
stops = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/stops.txt')
stop_times = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/stop_times.txt')
shapes = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/shapes.txt')
sdsheet = read.csv('/Users/sophia/Downloads/DSPROJECT/SDPublicTransportProject/data/updatedstops.csv')

routes = dbWriteTable(db, 'routes', routes, overwrite= TRUE)
stops = dbWriteTable(db, 'stops', stops, overwrite= TRUE)
stop_times = dbWriteTable(db, 'stop_times', stop_times, overwrite= TRUE)
shapes = dbWriteTable(db, 'shapes', shapes, overwrite= TRUE)
sdsheet = dbWriteTable(db, 'sdsheet', sdsheet, overwrite=TRUE)

dbGetQuery(db, 'select stop_id as stop from stop_times limit 10') 

dbGetQuery(db, 'select count(*) departure_time, stop_id as stop from stop_times group by stop_id')

dbGetQuery(db, 'select stop_times.stop_id from stop_times inner join stops on stop_times.stop_id = stops.stop_id')

dbGetQuery(db, 'select count(*) departure_time, sd.stop_id from stop_times s
           inner join sdsheet sd on s.stop_id = sd.stop_id
           group by sd.stop_id') 

dbGetQuery(db, 'select sd.stop_id, count(*) departure_time from stop_times s
           inner join sdsheet sd on s.stop_id = sd.stop_id
           group by sd.stop_id') #THIS IS THE ONE

dbGetQuery(db, 'select sd.stop_id, count(*) departure_time from sdsheet sd
           inner join stop_times s on s.stop_id = sd.stop_id
           group by sd.stop_id') #THIS IS THE ONE

dbGetQuery(db,'select stop_id, count(*) departure_time from stop_times where
stop_id = 12086')
