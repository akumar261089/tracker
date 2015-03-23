import bottle
import pymongo
from pymongo import MongoClient

#connect to database


@bottle.route('/')
def index():
    connection = MongoClient('localhost',27017)

    db = connection.track

    names = db.mytrack

    item = names.find_one()

    cr = [item['lat'][0],item['lng'][0]]
    return "<b>Coordinates %s </b>" %cr
#    return '<b>Coordinates %s </b>' %item["lng"][0]
bottle.run(host='localhost',port = 8082)


