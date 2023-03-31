library(DBI)
library(sqldf)
library(RSQLite)
setwd('/Users/sophia/Downloads/DSPROJECT/chroma')
drv = dbDriver('SQLite')
db = dbConnect(drv, dbname = 'gtfsdatabase.sqlite')

routes = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/routes.txt')
stops = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/stops.txt')
stop_times = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/stop_times.txt')
shapes = read.csv('/Users/sophia/Downloads/DSPROJECT/chroma/gtfsdata/shapes.txt')

routes = dbWriteTable(db, 'routes', routes, overwrite= TRUE)
stops = dbWriteTable(db, 'stops', stops, overwrite= TRUE)
stop_times = dbWriteTable(db, 'stop_times', stop_times, overwrite= TRUE)
shapes = dbWriteTable(db, 'shapes', shapes, overwrite= TRUE)

dbGetQuery(db, 'select * from routes limit 10')

