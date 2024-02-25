from flask import request, Response, jsonify
from bson import json_util, ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from repositories.mongo import mongo
from models.usuario import Usuario

def create(username, password, email, rol='comprador'):
    usuario = Usuario(username, password, email, rol)
    result = mongo.db.usuario.insert_one(usuario.to_dict())
    usuario._id = result.inserted_id
    return usuario

def update(user_id, new_password=None, new_email=None, new_rol=None):
    update_data = {}
    if new_password:
        update_data['password_hash'] = generate_password_hash(new_password)
    if new_email:
        update_data['email'] = new_email
    if new_rol:
        update_data['rol'] = new_rol
    
    mongo.db.usuario.update_one({'_id': user_id}, {'$set': update_data})


def delete(user_id):
    mongo.db.usuario.delete_one({'_id': user_id})


def getByUsername(username):
    usuario_doc = mongo.db.usuario.find_one({'username': username})
    if usuario_doc:
        return Usuario.from_mongo(usuario_doc)
    else:
        return None


def authenticate(username, password):
    usuario = getByUsername(username)
    if usuario and check_password_hash(usuario.password_hash, password):
        return usuario
    else:
        return None
    
def get_id(self):
    return str(self._id)