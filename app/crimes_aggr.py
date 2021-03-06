from pymongo import MongoClient
import pprint
import time


def aggregattion(hostname="localhost"):
    client = MongoClient("mongodb://" + hostname + ":27017")
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
        file.write("{},{}\n".format("aggregate-local", str(exec_time)))

    pprint.pprint(result)

    print("execution time: " + str(exec_time) + " seconds")


if __name__ == "__main__":
    aggregattion("mongodb_database")
