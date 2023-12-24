from math import e
from flask import request, jsonify

from src.models.productModel import Product
from . import productRoutes

@productRoutes.route('/api/products', methods=['POST', 'PUT'])
def multidata():
    try:
        # Update
        if request.method == 'PUT':
            if Product.update(request.json):
                return jsonify({
                    "status": 200
                })
            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400

        # Insert
        if request.method == 'POST':
            valid, msg = Product.create(request.json)
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

@productRoutes.route('/api/products/', methods=['GET'])
def getdata():
    try:
        kine = request.args.get("kine", None)
        dt = request.args.get("dt", None)
        print(kine)
        # Select by status
        if request.method == 'GET':
            valid, data = Product.select_by(kine, dt)
            if valid:
                return jsonify({
                    "status": 200,
                    "data": data
                })
            
            return jsonify({ 
                "error": "No se pudo completar la operacion" 
            }), 400

    except(e):
        return jsonify({ 
            "Message": "Ocurrio una excepcion en la ejecusion",
            "Error": e
        }), 503

@productRoutes.route('/api/products/<string:data>', methods=['DELETE'])
def data(data):
    try:           
        # Delete
        if request.method == 'DELETE':
            if Product.delete(data):
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