from app import db
from bson import json_util
import uuid
import json

class Order:

    def create(newData):
        order = {
            "_id": uuid.uuid4().hex,
            "order": int(newData['order']),
            "status": newData['status'],
            "items": newData['items']
        }

        if len(list(db.orders.find({ 'order': order['order'] }))) > 0:
            return False, "Numero de orden repetido | Orden: {}".format(order['order'])

        data = json.loads(json_util.dumps(db.products.find({})))
        for i in order["items"]:
            dbData = list(filter(lambda item: item['SKU'] == i['SKU'], data))
            
            if len(dbData)==0:
                return False, "No existe | SKU: {}".format(i["SKU"])

            if i["quantity"] > dbData[0]["quantity"]:
                return False, "No hay suficientes productos | SKU: {}".format(i["SKU"])

            upproduct = dbData[0]
            upproduct['quantity'] = dbData[0]['quantity'] - i['quantity']
            
            if not db.products.update_one({ '_id': dbData[0]['_id'] }, { '$set': upproduct }):
                return False, None
            
        if db.orders.insert_one(order):
            return True, None
        
        return False, None
    
    def update(newData):
        id = newData['_id']
        order = {
            "order": int(newData['order']),
            "status": newData['status'],
            "items": newData['items']
        }

        if db.orders.update_one({ '_id': id }, { '$set': order }):
            return True

        return False

    def select_by(stt):
        data = db.orders.find({'status': stt})

        if data:
            return True, json.loads(json_util.dumps(data))

        return False, ""

    def delete(id):
        if db.orders.delete_one({ '_id': id }):
            return True

        return False

    def order_number():
        data = db.orders.find().sort('order',-1).limit(1)
        
        if data:
            data = json.loads(json_util.dumps(data))
            norder = 1
            if len(data):
                data = data[0]
                norder = data['order'] + 1
            return True, norder
        
        return False

    def avalible_check(SKU, quantity):
        data = db.products.find({ "SKU": SKU })
        if data["quantity"] < quantity:
            return False

        return True