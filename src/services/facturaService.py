from bson import ObjectId
from datetime import datetime

from repositories.mongo import mongo
from models.factura import Factura


def getFacturaById(factura_id):
    factura_doc = mongo.db.factura.find_one({'_id': ObjectId(factura_id)})
    if factura_doc:
        return Factura.from_mongo(factura_doc)
    else:
        return None


def getFacturaAll():
 facturas = mongo.db.factura.find()
 result = []
 for factura in facturas:
    result.append(Factura.from_mongo(factura)) 

 r = [factura.to_dictFromBd() for factura in result]
 return r

def getAllByName(nombre):
 facturas = mongo.db.factura.find({"pedido.usuario.nombre": nombre})
 result = []
 for factura in facturas:
    result.append(Factura.from_mongo(factura)) 

 r = [factura.to_dictFromBd() for factura in result]
 return r


def crearFactura(pedido, forma_pago, usuario_actualizacion):
    factura = Factura(pedido, forma_pago, usuario_actualizacion)
    factDict = factura.to_dict()
    result = mongo.db.factura.insert_one(factDict)
    factura.id = result.inserted_id
    return factura