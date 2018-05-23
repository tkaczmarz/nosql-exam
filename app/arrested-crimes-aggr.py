from pymongo import MongoClient
import pprint
import time

client = MongoClient("mongodb://localhost:27017")
db = client.test

# aggregate
pipeline = [
    {'$match': {}},
    {'$group': {'_id': '$Primary_Type', 'crimes': {'$sum': 1}}}
]
start_time = time.time()
result = list(db.crimes.aggregate(pipeline))
exec_time = time.time() - start_time

with open('exec-times.csv', 'a') as file:
    file.write(str(exec_time) + "\n")

pprint.pprint(result)

print("execution time: " + str(exec_time) + " seconds")
