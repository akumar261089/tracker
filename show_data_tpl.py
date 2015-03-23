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
    len1 = len(item['lat'])
    cr = item['lat'][ len1 -1 ],item['lng'][ len1 -1]
    return bottle.template('main.html', {'cor':cr, 'name':item['name']})
#    return bottle.template('index', cor=item['lat'][len1 -1])
bottle.debug(True)
#    return '<b>Coordinates %s </b>' %item["lng"][0]
bottle.run(host='localhost',port = 8082)


