from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from datetime import datetime

class Usuario(UserMixin):
    def __init__(self, nombre, password, direccion, telefono, email, rol, categorizacion='low', fecha_creacion= datetime.now(), fecha_actualizacion= datetime.now()):
        self.nombre = nombre
        self.password = generate_password_hash(password)
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.categorizacion = categorizacion
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
        self.rol = rol

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'password': self.password,
            'email': self.email,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'categorizacion': self.categorizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion,
            'rol': self.rol
        }
    
    def to_dictFromBd(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'password': self.password,
            'email': self.email,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'categorizacion': self.categorizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion,
            'rol': self.rol
        }

    def from_mongo(doc):
        usuario=Usuario(doc['nombre'], doc['password'],  doc['direccion'], doc['telefono'],doc['email'], doc['rol'], doc['categorizacion'], doc['fecha_creacion'], doc['fecha_actualizacion'])
        usuario.id= doc['_id']
        usuario.password = doc['password']
        return usuario