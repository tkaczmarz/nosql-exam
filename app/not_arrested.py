from pymongo import MongoClient
import pprint

def not_arrested(hostname="localhost"):
    client = MongoClient("mongodb://" + hostname + ":27017")
    db = client.test

    # aggregate
    pipeline = [
        {'$match': {'Arrest': 'False'}},
        {'$group': {'_id': '$Primary_Type', 'not-arrested': {'$sum': 1}}}
    ]
    result = list(db.crimes.aggregate(pipeline))

    with open('not-arrested.csv', 'w') as csvfile:
        csvfile.write("sep=,\n")
        for row in result:
            csvfile.write("{},{}\n".format(row['_id'], row['not-arrested']))

    pprint.pprint(result)
