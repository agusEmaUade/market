from bson import ObjectId
from datetime import datetime

from repositories.mongo import mongo
from models.pedido import Pedido

def getPedidoById(pedido_id):
    pedido_doc = mongo.db.pedido.find_one({'_id': ObjectId(pedido_id)})
    if pedido_doc:
        return Pedido.from_mongo(pedido_doc)
    else:
        return None


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
    pedido.id = result.inserted_id
    return pedido

def updatePedido(product_id, new_usuario_actualizacion, new_estado):
    update_data = {}
  
    update_data['estado'] = new_estado
    update_data['fecha_actualizacion'] = datetime.now()
    update_data['usuario_actualizacion'] = new_usuario_actualizacion

    mongo.db.pedido.update_one({'_id': ObjectId(product_id)}, {'$set': update_data})