from datetime import datetime

class Producto:
    def __init__(self, nombre, descripcion, precio, cantidad, usuario_creacion, usuario_actualizacion, fecha_creacion= datetime.now(), fecha_actualizacion= datetime.now()):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.usuario_creacion = usuario_creacion
        self.usuario_actualizacion = usuario_actualizacion
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
       
       

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'usuario_creacion': self.usuario_creacion,
            'usuario_actualizacion': self.usuario_actualizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion

        }
    
    def to_dictFromBd(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'usuario_creacion': self.usuario_creacion,
            'usuario_actualizacion': self.usuario_actualizacion,
            'fecha_creacion': self.fecha_creacion,
            'fecha_actualizacion': self.fecha_actualizacion
        }
    
    def from_mongo(doc):
        producto = Producto(doc['nombre'], doc['descripcion'], doc['precio'], doc['cantidad'], doc['usuario_creacion'], doc['usuario_actualizacion'], doc['fecha_creacion'], doc['fecha_actualizacion'])
        producto.id= doc['_id']
        return producto