import pymongo

class Database:
    def connect():
        client = pymongo.MongoClient('localhost', 27017)
        return client.interactive