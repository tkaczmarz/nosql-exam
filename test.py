from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client.test

# insert data
# product1 = {
#     'product': 'bread',
#     'client': 'Pietrek',
#     'cost': 2.5
# }
# product2 = {
#     'product': 'potatos',
#     'client': 'Zbyszek',
#     'cost': 4
# }
# product3 = {
#     'product': 'bread',
#     'client': 'Zbyszek',
#     'cost': 2.8
# }
# result = db.testcol.insert_many([product1, product2, product3])

# aggregate
pipeline = [
    {"$match": {'client': 'Zbyszek'}},
    {'$group': {'_id': '$client', 'total': {'$sum': '$cost'}}}
]
result = list(db.testcol.aggregate(pipeline))

pprint.pprint(result)
