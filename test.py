from pymongo import MongoClient
import pprint
import bson

client = MongoClient("mongodb://localhost:27017")
db = client.test

# insert data
# product1 = {
#     'product': 'bread',
#     'client': 'Pietrek',
#     'cost': '2.5'
# }
# product2 = {
#     'product': 'potatos',
#     'client': 'Zbyszek',
#     'cost': '4'
# }
# product3 = {
#     'product': 'bread',
#     'client': 'Zbyszek',
#     'cost': '2.8'
# }
# result = test.insert_many([product1, product2, product3])

# aggregate
# cursor = db.test.aggregate([
#     {'$match': {'client': 'Zbyszek'}},
#     {'$group': {'_id': '$client', 'total': {'$sum': '$cost'}}}
# ])

cursor = db.testcol.aggregate([
    {'$group': {'_id': '$client', 'total': {'$sum': '$cost'}}}
])

pprint.pprint(cursor)

# for batch in cursor:
#     print(bson.decode_all(batch))
