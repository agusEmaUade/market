from bson import ObjectId
from datetime import datetime

from repositories.mongo import mongo
from models.producto import Producto


def getAllProduct():
 productos = mongo.db.producto.find()
 result = []
 for producto in productos:
    result.append(Producto.from_mongo(producto)) 

 r = [producto.to_dictFromBd() for producto in result]
 return r

def getAllActive():
 productos = mongo.db.producto.find({"cantidad": {"$gt": '0'}})
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

def create(nombre, descripcion, precio, cantidad, usuario_creacion, usuario_actualizacion):
    producto = Producto(nombre, descripcion, precio, cantidad, usuario_creacion, usuario_actualizacion)
    result = mongo.db.producto.insert_one(producto.to_dict())
    producto.id = result.inserted_id
    return producto


def update(product_id, new_usuario_actualizacion, new_nombre=None, new_descripcion=None, new_precio=None, new_cantidad=None):
    update_data = {}
    if new_nombre:
        update_data['nombre'] = new_nombre
    if new_descripcion:
        update_data['descripcion'] = new_descripcion
    if new_precio:
        update_data['precio'] = new_precio
    if new_cantidad:
        update_data['cantidad'] = new_cantidad

    update_data['fecha_actualizacion'] = datetime.now()
    update_data['usuario_actualizacion'] = new_usuario_actualizacion

    mongo.db.producto.update_one({'_id': ObjectId(product_id)}, {'$set': update_data})


def delete(product_id):
    mongo.db.producto.delete_one({'_id': ObjectId(product_id)})