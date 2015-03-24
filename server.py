
import sys
import datetime
import pymongo
from pymongo import MongoClient
connection = MongoClient('localhost',27017)
db = connection.track
names = db.mytrack
print ( names.find_one())
list(names.find())
name = raw_input('Enter Name')
cdate = input('Enter Date')
lat = input('Enter Latitude')
lng = input('Enter Longitude')
Id = input('Enter Id')
sdate = datetime.datetime.now().strftime( "%Y%m%d%H%M%S")

print ( name, cdate,lat,lng,Id,sdate)
names.update( {"name":name}, {"$push" : { "sdate":sdate, "cdate":cdate, "lat":lat, "lng":lng}})

#names.update( {"id":Id,"name":name}, {"$push" : { "sdate":sdate, "cdate":cdate, "lat":lat, "lng":lng}})
print ( names.find_one())
list(names.find())
