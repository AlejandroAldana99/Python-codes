#Importaciones
import pymongo                               
from bson.objectid import ObjectId           
from pymongo import MongoClient              
#import bson                                  

client = MongoClient('localhost',27017)      

db = client.test1                            
collection = db.test1                        
res = db.test1.distinct(                         
        #{                       
                #'_id': ObjectId('5c6b2b5c307157c9a94d8767')   
                'clinical_study.condition'          
                #}
        )
for consulta in res:                         
        print (consulta)                     
      

db = client.test1                            
collection = db.test1                        
res = db.test1.find(                         
        {                       
                #'_id': ObjectId('5c6b2b5c307157c9a94d8767')   
                'clinical_study.condition':{'$regex':'Lac'} 
                }
        )
for consulta in res:                         
        print (consulta)                     


db = client.test1                            
collection = db.test1                        
res = db.test1.find(
	{#'$or':[                     
                #'_id': ObjectId('5c6b2b5c307157c9a94d8767')   
                # {'clinical_study.condition':{'$regex':'Lac'}},
                # {'clinical_study.condition':{'$regex':'Sub'}}
                # ]
                }
        )
for consulta in res:                         
        print (consulta)  
