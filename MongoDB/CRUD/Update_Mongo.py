#Update a base de datos

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
#import bson
#import json

client = MongoClient('localhost',27017)

db = client.test1
collection = db.test1

db.test1.update(
        {
                '_id':ObjectId('5c6c36eb307157c9a94d91b7')
                },
         {
                 '$set':{'clinical_study.source':'Uno'}
         }
        )

res = db.test1.find()
for consulta in res:
        print (consulta)
