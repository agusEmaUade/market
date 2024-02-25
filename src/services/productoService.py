from flask import request, Response, jsonify
from bson import json_util, ObjectId

from repositories.mongo import mongo
from models.producto import Producto


def getAllActive():
 productos = mongo.db.producto.find()
 result = []
 for producto in productos:
    result.append(Producto.from_mongo(producto)) 

 r = [producto.to_dictFromBd() for producto in result]
 return r


def getByName(nombre: str):
    producto_doc = mongo.db.producto.find_one({'nombre': nombre})
    if producto_doc:
        producto = Producto.from_mongo(producto_doc)
        return producto.to_dictFromBd()
    else:
       return None

def getById(product_id):
    producto_doc = mongo.db.producto.find_one({'_id': ObjectId(product_id)})
    if producto_doc:
        return Producto.from_mongo(producto_doc)
    else:
        return None

def create(nombre, descripcion, precio):
    producto = Producto(nombre, descripcion, precio)
    result = mongo.db.producto.insert_one(producto.to_dict())
    producto._id = result.inserted_id
    return producto


def update(product_id, new_name=None, new_descripcion=None, new_precio=None):
    update_data = {}
    if new_name:
        update_data['nombre'] = new_name
    if new_descripcion:
        update_data['descripcion'] = new_descripcion
    if new_precio:
        update_data['precio'] = new_precio
    
    mongo.db.producto.update_one({'_id': product_id}, {'$set': update_data})


def delete(product_id):
    mongo.db.producto.delete_one({'_id': ObjectId(product_id)})