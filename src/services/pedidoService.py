from bson import ObjectId
from datetime import datetime

from repositories.mongo import mongo
from models.pedido import Pedido


def getAll():
 pedidos = mongo.db.pedido.find()
 result = []
 for pedido in pedidos:
    result.append(Pedido.from_mongo(pedido)) 

 r = [pedido.to_dictFromBd() for pedido in result]
 return r

def getAllByBuyer(nombre):
 pedidos = mongo.db.pedido.find({"usuario.nombre": nombre})
 result = []
 for pedido in pedidos:
    result.append(Pedido.from_mongo(pedido)) 

 r = [pedido.to_dictFromBd() for pedido in result]
 return r


def create(usuario, productos, montoTotal, usuario_actualizacion, cantidadItem):
    pedido = Pedido(usuario, productos, montoTotal, usuario_actualizacion, cantidadItem)
    result = mongo.db.pedido.insert_one(pedido.to_dict())
    pedido._id = result.inserted_id
    return pedido