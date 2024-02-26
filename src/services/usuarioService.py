from bson import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from repositories.mongo import mongo
from models.usuario import Usuario

def create(nombre, password, direccion, telefono, email, rol='comprador'):
    usuario = Usuario(nombre, password, direccion, telefono, email, rol)
    result = mongo.db.usuario.insert_one(usuario.to_dict())
    usuario.id = result.inserted_id
    return usuario

def update(user_id, new_nombre=None, new_password=None, new_direccion=None, new_telefono=None, new_email=None):
    update_data = {}
    if new_nombre:
        update_data['nombre'] = new_nombre
    if new_password:
        update_data['password'] = generate_password_hash(new_password)
    if new_direccion:
        update_data['direccion'] = new_direccion
    if new_telefono:
        update_data['telefono'] = new_telefono
    if new_email:
        update_data['email'] = new_email

    update_data['fecha_actualizacion'] = datetime.now()
    
    mongo.db.usuario.update_one({'_id': user_id}, {'$set': update_data})


def delete(user_id):
    mongo.db.usuario.delete_one({'_id': ObjectId(user_id)})


def getByUsername(nombre):
    usuario_doc = mongo.db.usuario.find_one({'nombre': nombre})
    if usuario_doc:
        return Usuario.from_mongo(usuario_doc)
    else:
        return None


def authenticate(nombre, password):
    usuario = getByUsername(nombre)
    if usuario and check_password_hash(usuario.password, password):
        return usuario
    else:
        return None
    
def getById(user_id):
    usuario_doc = mongo.db.usuario.find_one({'_id': ObjectId(user_id)})
    if usuario_doc:
        return Usuario.from_mongo(usuario_doc)
    else:
        return None

def getAllBuyers():
    usuarios_doc = mongo.db.usuario.find({'rol': 'comprador'})
    if usuarios_doc:
       result = []
       for user in usuarios_doc:
           result.append(Usuario.from_mongo(user))
       
       r = [user.to_dictFromBd() for user in result]
       return r
    else:
       return None