from flask import request, Response, jsonify
from bson import json_util, ObjectId

from repositories.mongo import mongo


def get_todos_service():
    data = mongo.db.producto.find()

    #convierto la data en diccionario
    productos = [doc for doc in data]
    
    return productos