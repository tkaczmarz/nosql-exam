from pymongo import MongoClient
import pprint
from bson.code import Code
import time

client = MongoClient("mongodb://localhost:27017")
db = client.test

# map function
mapper = Code("""
            function () {
                emit(this.Primary_Type, this.Arrest);
            }
            """)

# reduce function
reducer = Code("""
                function (key, values) {
                    var count = 0;
                    for (var i = 0; i < values.length; i++) {
                        if (values[i] == "True") count++; 
                    }
                    return count;
                }
                """)

# map reduce
start_time = time.time()
result = db.crimes.map_reduce(mapper, reducer, 'results')
exec_time = time.time() - start_time

for doc in result.find():
    pprint.pprint(doc)

print("execution time: " + str(exec_time) + " seconds")
