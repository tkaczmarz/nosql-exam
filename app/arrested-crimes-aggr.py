from pymongo import MongoClient
import pprint
import time

client = MongoClient("mongodb://localhost:27017")
db = client.test

# aggregate
pipeline = [
    {'$match': {'Arrest': 'True'}},
    {'$group': {'_id': '$Primary_Type', 'arrests': {'$sum': 1}}},
    {'$sort': {'arrests': -1}}
]
start_time = time.time()
result = list(db.crimes.aggregate(pipeline))
exec_time = time.time() - start_time

pprint.pprint(result)

print("execution time: " + str(exec_time) + " seconds")
