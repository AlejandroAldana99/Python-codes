from app import db
from bson import json_util
import uuid
import json

class Product:

    def create(newData):
        product = {
            "_id": uuid.uuid4().hex,
            "quantity": int(newData['quantity']),
            "SKU": newData['SKU'],
            "name": newData['name']
        }

        data = db.products.find({ "SKU": product['SKU'] })
        if len(list(data)) != 0:
            return False, "SKU Repetido"

        if db.products.insert_one(product):
            return True, None
        
        return False, None
    
    def update(newData):
        id = newData['_id']

        product = {
            "quantity": int(newData['quantity']),
            "SKU": newData['SKU'],
            "name": newData['name']
        }

        if db.products.update_one({ '_id': id }, { '$set': product }):
            return True

        return False

    def select_by(kine, dt):
        query = {}
        if kine == "SKU":
            query = { "SKU": dt }
        elif kine == "id": 
            query = { "_id": dt }
        
        data = db.products.find(query)

        if data:
            return True, json.loads(json_util.dumps(data))

        return False, ""

    def delete(id):
        if db.products.delete_one({ '_id': id }):
            return True

        return False
        
        