from flask import request, Response, jsonify
from bson import json_util, ObjectId

from repositories.mongo import mongo
from models.producto import Producto


def getAllActive():
 productos = mongo.db.producto.find()
 result = []
 for producto in productos:
    result.append(Producto.from_mongo(producto)) 
 print(result)
 r = [producto.to_dict() for producto in result]
 print(r)  
 return r


def getByName(nombre: str):
    producto_doc = mongo.db.producto.find_one({'nombre': nombre})
    if producto_doc:
        producto = Producto.from_mongo(producto_doc)
        return producto.to_dict()
    else:
       return None
        
