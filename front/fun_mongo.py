import pymongo

my_client = pymongo.MongoClient('mongodb://root:123@10.93.53.187:27017/')
my_db = my_client['db_ships']
my_collection = my_db['test']

r = list(my_collection.find())

print(r)
