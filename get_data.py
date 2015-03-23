import pymongo
from pymongo import MongoClient

#connect to database

connection = MongoClient('localhost',27017)
db = connection.track
names = db.mytrack
item = names.find_one()
print item["lat"][1],",", item["lng"][1]



