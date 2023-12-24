from math import e
from flask import request, jsonify

from src.models.orderModel import Order
from . import orderRoutes

@orderRoutes.route('/api/orders', methods=['POST', 'PUT'])
def multidata():
    try:
        # Update
        if request.method == 'PUT':
            if Order.update(request.json):
                return jsonify({
                    "status": 200
                })
            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400

        # Insert
        if request.method == 'POST':
            valid, msg = Order.create(request.json)
            if valid:
                return jsonify({
                    "status": 200
                })
            elif msg != None:
                return jsonify({
                    "message": msg
                }), 400
            
            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400

    except(e):
        return jsonify({ 
            "Message": "Ocurrio una excepcion en la ejecución",
            "Error": e
        }), 503

@orderRoutes.route('/api/orders/<string:data>', methods=['GET', 'DELETE'])
def data(data):
    try:
        # Select by status
        if request.method == 'GET':
            valid, data = Order.select_by(data)
            if valid:
                return jsonify({
                    "status": 200,
                    "data": data
                })
            
            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400
            
        # Delete
        if request.method == 'DELETE':
            if Order.delete(data):
                return jsonify({
                    "status": 200
                })

            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400

    except(e):
        return jsonify({ 
            "Message": "Ocurrio una excepcion en la ejecusion",
            "Error": e
        }), 503

@orderRoutes.route('/api/norder', methods=['GET'])
def onedata():
    try:
        # Select order number
        if request.method == 'GET':
            valid, n = Order.order_number()
            if valid:
                return jsonify({
                    "status": 200,
                    "n": n
                })
            
            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400

    except(e):
        return jsonify({ 
            "Message": "Ocurrio una excepcion en la ejecusion",
            "Error": e
        }), 503