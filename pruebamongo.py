import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

mibase = client['nuevabase']
micoll = mibase['usuarios']
midict = { "name": "John", "pass": "nontefixes" }

x = micoll.insert_one(midict)
