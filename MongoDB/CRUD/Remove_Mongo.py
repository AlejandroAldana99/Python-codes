#Insert a base de datos

import pymongo
import bson
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost',27017)

db = client.test1
collection = db.test1
ins = db.test1.remove(
        {
                #'_id': ObjectId('5c682d7e039e174d39f67088')
                'clinical_study.source':'1'
                }
        )
res = db.test1.find()
for consulta in res:
        print (consulta)
