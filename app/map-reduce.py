from pymongo import MongoClient
from bson.code import Code
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

# map function
mapper = Code("""
            function () {
                emit(this.product, this.cost);
            }
            """)

# reduce function
reducer = Code("""
                function (key, values) {
                    return Array.sum(values);
                }
                """)

# map reduce
result = db.testcol.map_reduce(mapper, reducer, 'results')

for doc in result.find():
    pprint.pprint(doc)
