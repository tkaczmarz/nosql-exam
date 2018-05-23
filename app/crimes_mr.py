from pymongo import MongoClient
import pprint
from bson.code import Code
import time

def map_reduce(hostname="localhost"):
    client = MongoClient("mongodb://" + hostname + ":27017")
    db = client.test

    # map function
    mapper = Code("""
                function () {
                    emit(this.Primary_Type, 1);
                }
                """)

    # reduce function
    reducer = Code("""
                    function (key, values) {
                        return Array.sum(values);
                        var sum = 0;
                        for(var i in values)
                        sum += 1;
                        return sum;
                    }
                    """)

    # map reduce
    start_time = time.time()
    result = db.crimes.map_reduce(mapper, reducer, "arrests")
    exec_time = time.time() - start_time
    l = list(result.find())

    with open('crimes-mr.csv', 'w') as csvfile:
        csvfile.write("sep=,\n")
        for row in l:
            csvfile.write("{},{}\n".format(row['_id'], row['value']))

    with open('exec-times.csv', 'a') as file:
        file.write("sep=,\n")
        file.write("{},{}\n".format("map-reduce-local", str(exec_time)))

    pprint.pprint(l)

    print("execution time: " + str(exec_time) + " seconds")
