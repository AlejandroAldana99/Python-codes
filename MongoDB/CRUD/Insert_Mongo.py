#Insert a base de datos

import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

client = MongoClient('localhost',27017)

db = client.ai_intents
collection = db.ai_intents

# Data = json.loads(open
#                   (r'C:/Users/baker/Downloads/Lion10/CTsXmlToJson/json1/NCT00015067.json'
#                    ).read())

# ins = db.test1.insert(

db.ai_intents.insert('patterns' :{
    [ "Hi" ],
    #"responses" : [ "Hi, thanks for visiting", "Hi there, how can I help?", "Hello", "Hey" ], 
})
                #{'nombre':dato1,'apellido':dato2,'compañia':dato3}
                # Data
        # )

res = db.test1.find()
for consulta in res:
        print (consulta)
